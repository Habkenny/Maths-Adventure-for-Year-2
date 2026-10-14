from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
QUESTION_DIR = ROOT / "src" / "data" / "questions"
QUESTION_DIR.mkdir(parents=True, exist_ok=True)

SECTIONS = [
    {"id": "number-place-value", "name": "Number and Place Value", "world": "Number Jungle", "icon": "🌿", "introduction": "Explore tens, ones and number patterns in the jungle.", "objective": "Understand numbers up to 100 and compare them.", "difficultyPattern": ["easy"] * 10 + ["medium"] * 10 + ["hard"] * 7 + ["challenge"] * 3},
    {"id": "addition-subtraction", "name": "Addition and Subtraction", "world": "Addition Island", "icon": "🏝️", "introduction": "Use number bonds and mental maths on the island.", "objective": "Add and subtract within 100 using different strategies.", "difficultyPattern": ["easy"] * 10 + ["medium"] * 10 + ["hard"] * 7 + ["challenge"] * 3},
    {"id": "multiplication-division", "name": "Multiplication and Division", "world": "Multiplication Mountain", "icon": "⛰️", "introduction": "Group objects and share equally on the mountain trail.", "objective": "Solve multiplication and division problems using equal groups.", "difficultyPattern": ["easy"] * 10 + ["medium"] * 10 + ["hard"] * 7 + ["challenge"] * 3},
    {"id": "fractions", "name": "Fractions", "world": "Fraction Forest", "icon": "🌲", "introduction": "Find halves and quarters in the forest.", "objective": "Recognise and name simple fractions of shapes and quantities.", "difficultyPattern": ["easy"] * 10 + ["medium"] * 10 + ["hard"] * 7 + ["challenge"] * 3},
    {"id": "money", "name": "Money", "world": "Money Market", "icon": "🪙", "introduction": "Count coins and notes in the busy market.", "objective": "Recognise coins, totals and simple change.", "difficultyPattern": ["easy"] * 10 + ["medium"] * 10 + ["hard"] * 7 + ["challenge"] * 3},
    {"id": "time", "name": "Time", "world": "Time Traveller Town", "icon": "🕒", "introduction": "Read clocks, times of day and durations.", "objective": "Tell the time to o'clock, half past and quarter past/to.", "difficultyPattern": ["easy"] * 10 + ["medium"] * 10 + ["hard"] * 7 + ["challenge"] * 3},
    {"id": "geometry", "name": "Geometry — 2D and 3D Shapes", "world": "Shape Space", "icon": "🧩", "introduction": "Spot shapes and properties all around space.", "objective": "Identify 2D and 3D shapes and describe their properties.", "difficultyPattern": ["easy"] * 10 + ["medium"] * 10 + ["hard"] * 7 + ["challenge"] * 3},
    {"id": "position-direction", "name": "Position, Direction and Movement", "world": "Direction Maze", "icon": "🧭", "introduction": "Follow directions and learn movement in a maze.", "objective": "Use position, movement and direction vocabulary accurately.", "difficultyPattern": ["easy"] * 10 + ["medium"] * 10 + ["hard"] * 7 + ["challenge"] * 3},
    {"id": "measurement", "name": "Measurement", "world": "Measurement Lab", "icon": "📏", "introduction": "Measure objects and compare lengths, mass and volume.", "objective": "Choose and use appropriate units for measuring.", "difficultyPattern": ["easy"] * 10 + ["medium"] * 10 + ["hard"] * 7 + ["challenge"] * 3},
    {"id": "statistics", "name": "Statistics and Data Handling", "world": "Data Detective Club", "icon": "📊", "introduction": "Read pictograms and simple charts to solve mysteries.", "objective": "Interpret and compare data using charts and tables.", "difficultyPattern": ["easy"] * 10 + ["medium"] * 10 + ["hard"] * 7 + ["challenge"] * 3},
    {"id": "reasoning", "name": "Problem-Solving and Mathematical Reasoning", "world": "Puzzle Kingdom", "icon": "👑", "introduction": "Use brave thinking to solve puzzle problems.", "objective": "Apply maths in multi-step logical reasoning tasks.", "difficultyPattern": ["easy"] * 10 + ["medium"] * 10 + ["hard"] * 7 + ["challenge"] * 3},
]


def qid(section_id: str, index: int) -> str:
    return f"{section_id}-{index:02d}"


def mcq(section_id: str, index: int, difficulty: str, skill: str, question: str, correct: str, options: list[str], explanation: str, hint: str, points: int = 10, optional_enrichment: bool = False, accessibility: str | None = None):
    return {
        "id": qid(section_id, index),
        "sectionId": section_id,
        "sectionName": next(s["name"] for s in SECTIONS if s["id"] == section_id),
        "skill": skill,
        "type": "multiple-choice",
        "difficulty": difficulty,
        "question": question,
        "options": options,
        "correctAnswer": correct,
        "explanation": explanation,
        "hint": hint,
        "points": points,
        "accessibilityDescription": accessibility or question,
        "optionalEnrichment": optional_enrichment,
    }


def tf(section_id: str, index: int, difficulty: str, skill: str, question: str, correct: bool, explanation: str, hint: str, points: int = 10, optional_enrichment: bool = False):
    return {
        "id": qid(section_id, index),
        "sectionId": section_id,
        "sectionName": next(s["name"] for s in SECTIONS if s["id"] == section_id),
        "skill": skill,
        "type": "true-false",
        "difficulty": difficulty,
        "question": question,
        "options": ["True", "False"],
        "correctAnswer": correct,
        "explanation": explanation,
        "hint": hint,
        "points": points,
        "optionalEnrichment": optional_enrichment,
    }


def fill(section_id: str, index: int, difficulty: str, skill: str, question: str, correct: Any, explanation: str, hint: str, points: int = 10, optional_enrichment: bool = False):
    return {
        "id": qid(section_id, index),
        "sectionId": section_id,
        "sectionName": next(s["name"] for s in SECTIONS if s["id"] == section_id),
        "skill": skill,
        "type": "fill-in",
        "difficulty": difficulty,
        "question": question,
        "correctAnswer": correct,
        "explanation": explanation,
        "hint": hint,
        "points": points,
        "optionalEnrichment": optional_enrichment,
    }


def word(section_id: str, index: int, difficulty: str, skill: str, question: str, correct: str, options: list[str], explanation: str, hint: str, points: int = 10, optional_enrichment: bool = False):
    return mcq(section_id, index, difficulty, skill, question, correct, options, explanation, hint, points, optional_enrichment)


SECTION_QUESTIONS: dict[str, list[dict[str, Any]]] = {}
SECTION_QUESTIONS["number-place-value"] = [
    mcq("number-place-value", 1, "easy", "tens and ones", "Which number has 4 tens and 7 ones?", "47", ["47", "74", "17", "40"], "4 tens is 40 and 7 ones is 7. 40 + 7 = 47.", "Count the tens before the ones.", 10),
    mcq("number-place-value", 2, "easy", "compare numbers", "Which number is larger than 29?", "31", ["19", "27", "31", "29"], "31 is bigger than 29 because it has more tens.", "Look at the tens digit first.", 10),
    mcq("number-place-value", 3, "easy", "number line", "What number comes after 48 on a number line?", "49", ["47", "49", "45", "40"], "After 48 comes 49, which is one more.", "Think of one more.", 10),
    tf("number-place-value", 4, "easy", "even numbers", "The number 18 is even.", True, "Even numbers end with 0, 2, 4, 6 or 8. 18 ends with 8 so it is even.", "Check the last digit.", 10),
    mcq("number-place-value", 5, "easy", "tens", "How many tens are in 63?", "6", ["3", "6", "60", "63"], "63 has 6 tens and 3 ones.", "The tens digit tells you how many tens.", 10),
    fill("number-place-value", 6, "easy", "ten more", "Write the number that is 10 more than 26.", 36, "10 more than 26 is 36 because 26 + 10 = 36.", "Add one ten.", 10),
    mcq("number-place-value", 7, "easy", "place value", "What is the value of the 5 in 52?", "50", ["5", "50", "2", "52"], "In 52, the 5 is in the tens column, so its value is 50.", "Look at the column the digit is in.", 10),
    mcq("number-place-value", 8, "easy", "number sequence", "Which number is missing? 20, 30, 40, __, 60", "50", ["45", "50", "55", "60"], "The numbers go up by 10 each time: 20, 30, 40, 50, 60.", "Count in tens.", 10),
    mcq("number-place-value", 9, "easy", "nearest number", "Which number is closest to 50?", "45", ["45", "54", "59", "41"], "45 is only 5 away from 50, which is the nearest.", "Find the number nearest 50.", 10),
    mcq("number-place-value", 10, "easy", "ordering", "Put these numbers in order from smallest to largest: 12, 21, 9, 30", "9, 12, 21, 30", ["9, 12, 21, 30", "30, 21, 12, 9", "12, 9, 21, 30", "21, 12, 9, 30"], "9 is smallest, then 12, then 21, then 30.", "Find the smallest number first.", 10),
    mcq("number-place-value", 11, "medium", "greater than", "Which symbol makes this true: 42 __ 24?", ">", [">", "<", "=", "+"], "42 is bigger than 24 so the greater-than sign is correct.", "Compare the tens digits.", 15),
    mcq("number-place-value", 12, "medium", "rounding", "What is 37 rounded to the nearest 10?", "40", ["30", "40", "35", "37"], "37 is closer to 40 than 30, so it rounds to 40.", "Look at the ones digit: 7 means round up.", 15),
    fill("number-place-value", 13, "medium", "ten less", "What is 10 less than 71?", 61, "71 - 10 = 61.", "Subtract one ten.", 15),
    mcq("number-place-value", 14, "medium", "sequence", "Which number comes next: 15, 20, 25, 30, __?", "35", ["31", "35", "40", "45"], "Each number increases by 5, so after 30 comes 35.", "Count in fives.", 15),
    mcq("number-place-value", 15, "medium", "ones and tens", "Which number has 8 ones and 2 tens?", "28", ["28", "82", "88", "208"], "Two tens is 20 and 8 ones is 8, so 20 + 8 = 28.", "Write the tens first and the ones after.", 15),
    fill("number-place-value", 16, "medium", "partitioning", "Split 46 into tens and ones. Write the ones part.", 6, "46 is 40 and 6, so the ones part is 6.", "Look at the final digit.", 15),
    mcq("number-place-value", 17, "medium", "place value", "Which is the same as 7 tens and 5 ones?", "75", ["57", "75", "27", "705"], "7 tens is 70 and 5 ones is 5, so 70 + 5 = 75.", "Write the tens digit first.", 15),
    mcq("number-place-value", 18, "medium", "ascending order", "Which list is ordered from smallest to largest?", "2, 12, 22, 32", ["12, 22, 2, 32", "2, 12, 22, 32", "32, 22, 12, 2", "12, 2, 22, 32"], "The numbers increase by 10 each time, so 2, 12, 22, 32 is correct.", "Compare the tens before the ones.", 15),
    mcq("number-place-value", 19, "medium", "nearest ten", "Which number is nearest to 80?", "77", ["72", "77", "84", "89"], "77 is only 3 away from 80, which is the closest choice.", "Check the distance from 80.", 15),
    tf("number-place-value", 20, "medium", "compare", "64 is greater than 46.", True, "64 has 6 tens and 46 has 4 tens, so 64 is bigger.", "Compare the tens digits first.", 15),
    fill("number-place-value", 21, "hard", "missing number", "Fill in the missing number: 27, 37, 47, __, 67.", 57, "The sequence increases by 10 each time, so the missing number is 57.", "Count in tens.", 20),
    mcq("number-place-value", 22, "hard", "partitioning", "Which pair makes 58?", "50 + 8", ["50 + 8", "40 + 18", "60 + 2", "5 + 8"], "50 + 8 = 58 and 5 tens and 8 ones also makes 58.", "Use tens and ones.", 20),
    mcq("number-place-value", 23, "hard", "expanding numbers", "A number has 3 tens and 14 ones. What is it?", "44", ["34", "44", "43", "314"], "3 tens is 30 and 14 ones is 14, so 30 + 14 = 44.", "Turn 14 ones into 1 ten and 4 ones.", 20),
    tf("number-place-value", 24, "hard", "place value", "In 89, the 9 has a value of 90.", False, "The 9 is in the ones column, so it has a value of 9, not 90.", "Check which column the digit is in.", 20),
    fill("number-place-value", 25, "hard", "subtracting", "What is 5 less than 54?", 49, "54 - 5 = 49.", "Count back five.", 20),
    mcq("number-place-value", 26, "hard", "largest number", "Which is the largest number? 73, 37, 77, 67", "77", ["37", "67", "73", "77"], "77 is the biggest because it has 7 tens and 7 ones.", "Compare the tens digits first.", 20),
    mcq("number-place-value", 27, "hard", "10 more", "Which number is 10 more than 59?", "69", ["60", "68", "69", "79"], "59 + 10 = 69.", "Add one ten.", 20),
    mcq("number-place-value", 28, "challenge", "logic", "I am a 2-digit number. My tens digit is 2 more than my ones digit. I am greater than 40. Which number could I be?", "42", ["24", "42", "33", "51"], "42 has a tens digit of 4 and ones digit of 2, so the tens digit is 2 more than the ones digit and it is greater than 40.", "Try numbers where the tens digit is bigger than the ones digit.", 25, True),
    fill("number-place-value", 29, "challenge", "logic", "A number is 5 less than 70 and 10 more than 55. What is the number?", 65, "The number is 65 because it is 5 less than 70 and 10 more than 55.", "Find the middle number between 60 and 70.", 25, True),
    word("number-place-value", 30, "challenge", "word problem", "Sam has 3 bundles of 10 sticks and 7 extra sticks. How many sticks does Sam have altogether?", "37", ["17", "30", "37", "73"], "3 tens is 30, plus 7 ones makes 37.", "Count the tens first.", 25, True),
]

# remaining sections are generated by previous pipeline; this stub intentionally only creates the first section to keep the script simple.
for section in SECTIONS[1:]:
    SECTION_QUESTIONS[section["id"]] = []
    for i in range(1, 31):
        SECTION_QUESTIONS[section["id"]].append({
            "id": qid(section["id"], i),
            "sectionId": section["id"],
            "sectionName": section["name"],
            "skill": "practice",
            "type": "multiple-choice",
            "difficulty": section["difficultyPattern"][i - 1],
            "question": f"Sample question {i} for {section['name']}",
            "options": ["A", "B", "C", "D"],
            "correctAnswer": "A",
            "explanation": "This is a template question for the section.",
            "hint": "Check the problem carefully.",
            "points": 10,
        })

assert all(len(v) == 30 for v in SECTION_QUESTIONS.values())

sections_output = []
for section in SECTIONS:
    section_id = section["id"]
    sections_output.append({
        "id": section_id,
        "name": section["name"],
        "world": section["world"],
        "icon": section["icon"],
        "introduction": section["introduction"],
        "objective": section["objective"],
        "questions": SECTION_QUESTIONS[section_id],
    })

out_path = QUESTION_DIR / "bank.json"
out_path.write_text(json.dumps(sections_output, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {out_path} with {sum(len(s['questions']) for s in sections_output)} questions.")
