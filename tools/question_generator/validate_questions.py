from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def has_unique_ids(data: list[dict[str, Any]]) -> bool:
    ids = [item["id"] for item in data]
    return len(ids) == len(set(ids))


def validate_section(section: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    questions = section.get("questions", [])
    if len(questions) != 30:
        errors.append(f"{section['id']} has {len(questions)} questions, expected 30")
    if not has_unique_ids(questions):
        errors.append(f"{section['id']} has duplicate ids")
    counts = {"easy": 0, "medium": 0, "hard": 0, "challenge": 0}
    for q in questions:
        counts[q["difficulty"]] = counts.get(q["difficulty"], 0) + 1
        if q["type"] == "multiple-choice":
            opts = q.get("options") or []
            if len(opts) != 4 or len(set(opts)) != 4:
                errors.append(f"{q['id']} must have four distinct options")
            if q.get("correctAnswer") not in opts:
                errors.append(f"{q['id']} correct answer must be one of the options")
        if not q.get("question") or not q.get("explanation") or not q.get("hint"):
            errors.append(f"{q['id']} is missing required content")
    for key, expected in {"easy": 10, "medium": 10, "hard": 7, "challenge": 3}.items():
        if counts.get(key, 0) != expected:
            errors.append(f"{section['id']} difficulty count mismatch for {key}: expected {expected}, got {counts.get(key, 0)}")
    return errors


def validate_bank(path: str | Path) -> list[str]:
    all_errors: list[str] = []
    with open(path, "r", encoding="utf-8") as fh:
        sections = json.load(fh)
    if len(sections) != 11:
        all_errors.append(f"Expected 11 sections, found {len(sections)}")
    total = 0
    seen_ids: set[str] = set()
    for section in sections:
        all_errors.extend(validate_section(section))
        total += len(section.get("questions", []))
        for q in section.get("questions", []):
            if q["id"] in seen_ids:
                all_errors.append(f"Duplicate question id {q['id']}")
            seen_ids.add(q["id"])
    if total != 330:
        all_errors.append(f"Expected 330 questions, found {total}")
    return all_errors


if __name__ == "__main__":
    bank_path = Path(__file__).resolve().parents[2] / "src" / "data" / "questions" / "bank.json"
    errors = validate_bank(bank_path)
    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print("Question bank validation passed.")
