from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

Difficulty = Literal["easy", "medium", "hard", "challenge"]
QuestionType = Literal["multiple-choice", "fill-in", "true-false", "ordering", "matching", "visual-puzzle", "word-problem"]


@dataclass
class VisualData:
    type: str
    title: str | None = None
    values: list[Any] | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class Question:
    id: str
    sectionId: str
    sectionName: str
    skill: str
    type: QuestionType
    difficulty: Difficulty
    question: str
    correctAnswer: Any
    explanation: str
    hint: str
    points: int
    options: list[str] | None = None
    visual: VisualData | None = None
    accessibilityDescription: str | None = None
    optionalEnrichment: bool = False
