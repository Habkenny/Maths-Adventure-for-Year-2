from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'src' / 'data' / 'questions' / 'bank.json'
OUT.parent.mkdir(parents=True, exist_ok=True)

SECTIONS = [
    {'id': 'number-place-value', 'name': 'Number and Place Value', 'world': 'Number Jungle', 'icon': '🌿', 'introduction': 'Explore tens, ones and number patterns in the jungle.', 'objective': 'Understand numbers up to 100 and compare them.'},
    {'id': 'addition-subtraction', 'name': 'Addition and Subtraction', 'world': 'Addition Island', 'icon': '🏝️', 'introduction': 'Use number bonds and mental maths on the island.', 'objective': 'Add and subtract within 100 using different strategies.'},
    {'id': 'multiplication-division', 'name': 'Multiplication and Division', 'world': 'Multiplication Mountain', 'icon': '⛰️', 'introduction': 'Group objects and share equally on the mountain trail.', 'objective': 'Solve multiplication and division problems using equal groups.'},
    {'id': 'fractions', 'name': 'Fractions', 'world': 'Fraction Forest', 'icon': '🌲', 'introduction': 'Find halves and quarters in the forest.', 'objective': 'Recognise and name simple fractions of shapes and quantities.'},
    {'id': 'money', 'name': 'Money', 'world': 'Money Market', 'icon': '🪙', 'introduction': 'Count coins and notes in the busy market.', 'objective': 'Recognise coins, totals and simple change.'},
    {'id': 'time', 'name': 'Time', 'world': 'Time Traveller Town', 'icon': '🕒', 'introduction': 'Read clocks, times of day and durations.', 'objective': 'Tell the time to o'clock, half past and quarter past/to.'},
    {'id': 'geometry', 'name': 'Geometry — 2D and 3D Shapes', 'world': 'Shape Space', 'icon': '🧩', 'introduction': 'Spot shapes and properties all around space.', 'objective': 'Identify 2D and 3D shapes and describe their properties.'},
    {'id': 'position-direction', 'name': 'Position, Direction and Movement', 'world': 'Direction Maze', 'icon': '🧭', 'introduction': 'Follow directions and learn movement in a maze.', 'objective': 'Use position, movement and direction vocabulary accurately.'},
    {'id': 'measurement', 'name': 'Measurement', 'world': 'Measurement Lab', 'icon': '📏', 'introduction': 'Measure objects and compare lengths, mass and volume.', 'objective': 'Choose and use appropriate units for measuring.'},
    {'id': 'statistics', 'name': 'Statistics and Data Handling', 'world': 'Data Detective Club', 'icon': '📊', 'introduction': 'Read pictograms and simple charts to solve mysteries.', 'objective': 'Interpret and compare data using charts and tables.'},
    {'id': 'reasoning', 'name': 'Problem-Solving and Mathematical Reasoning', 'world': 'Puzzle Kingdom', 'icon': '👑', 'introduction': 'Use brave thinking to solve puzzle problems.', 'objective': 'Apply maths in multi-step logical reasoning tasks.'},
]

DIFFICULTY_ORDER = ['easy'] * 10 + ['medium'] * 10 + ['hard'] * 7 + ['challenge'] * 3
QUESTION_TYPES = ['multiple-choice', 'fill-in', 'true-false', 'word-problem']

SECTION_FACTS = {
    'number-place-value': {'skill': 'place value', 'base': 10, 'delta': 5, 'example': 'tens and ones'},
    'addition-subtraction': {'skill': 'number bonds', 'base': 8, 'delta': 3, 'example': 'addition and subtraction'},
    'multiplication-division': {'skill': 'equal groups', 'base': 2, 'delta': 4, 'example': 'times tables'},
    'fractions': {'skill': 'fractions', 'base': 4, 'delta': 2, 'example': 'halves and quarters'},
    'money': {'skill': 'money', 'base': 10, 'delta': 5, 'example': 'coins and totals'},
    'time': {'skill': 'time', 'base': 15, 'delta': 10, 'example': 'clock reading'},
    'geometry': {'skill': 'shapes', 'base': 3, 'delta': 2, 'example': '2D and 3D shapes'},
    'position-direction': {'skill': 'direction', 'base': 2, 'delta': 3, 'example': 'left, right and turns'},
    'measurement': {'skill': 'measurement', 'base': 10, 'delta': 5, 'example': 'length and mass'},
    'statistics': {'skill': 'data', 'base': 2, 'delta': 3, 'example': 'charts and pictograms'},
    'reasoning': {'skill': 'reasoning', 'base': 5, 'delta': 2, 'example': 'patterns and logic'},
}


def question_for(sec_id: str, index: int, difficulty: str):
    facts = SECTION_FACTS[sec_id]
    base = facts['base'] + (index % 6) * facts['delta']
    if sec_id == 'number-place-value':
        num = base + (index % 5)
        if index % 4 == 0:
            q = f"Which number is 10 more than {num}?"
           opts = [str(num + 10), str(num + 1), str(num - 10), str(num)]
            answer = str(num + 10)
            explanation = f"{num} plus 10 is {num + 10}."
        elif index % 4 == 1:
            q = f"What is the value of the tens digit in {num + 20}?"
            opts = [str((num + 20) // 10 * 10), str(num), str((num + 20) % 10), str(num + 20)]
            answer = str((num + 20) // 10 * 10)
            explanation = f"In {(num + 20)}, the tens digit is worth {(num + 20) // 10 * 10}."
        elif index % 4 == 2:
            q = f"Which number is smaller than {num + 15}?"
            opts = [str(num + 16), str(num + 15), str(num + 13), str(num + 20)]
            answer = str(num + 13)
            explanation = f"{num + 13} is less than {num + 15}."
        else:
            q = f"Which number comes next: {num}, {num + 5}, {num + 10}, __ ?"
            opts = [str(num + 15), str(num + 5), str(num + 20), str(num + 1)]
            answer = str(num + 15)
            explanation = f"The sequence increases by 5 each time, so the next is {num + 15}."
    elif sec_id == 'addition-subtraction':
        a = base + index
        b = base + 2
        if index % 4 == 0:
            q = f"What is {a} + {b}?"
            answer = str(a + b)
            opts = [str(a + b), str(a + b - 2), str(a + b + 3), str(a + b + 10)]
            explanation = f"{a} plus {b} equals {a + b}."
        elif index % 4 == 1:
            q = f"What is {a + 10} - {b}?"
            answer = str(a + 10 - b)
            opts = [str(a + 10 - b), str(a + 10 - b + 2), str(a + 10 - b + 4), str(a + 10 - b + 7)]
            explanation = f"Subtracting {b} from {a + 10} gives {a + 10 - b}."
        elif index % 4 == 2:
            q = f"What number makes {a} + __ = {a + 8}?"
            answer = '8'
            opts = ['8', '7', '9', '5']
            explanation = f"{a} plus 8 equals {a + 8}."
        else:
            q = f"What is {a + 5} - {a - 2}?"
            answer = '7'
            opts = ['6', '7', '8', '9']
            explanation = f"{a + 5} minus {a - 2} is 7."
    elif sec_id == 'multiplication-division':
        a = base + 1
        b = 2 + (index % 4)
        if index % 4 == 0:
            q = f"What is {a} x {b}?"
            answer = str(a * b)
            opts = [str(a * b), str(a * b - 2), str(a * b + 1), str(a * b + 5)]
            explanation = f"{a} groups of {b} is {a * b}."
        elif index % 4 == 1:
            q = f"What is {a * b} ÷ {b}?"
            answer = str(a)
            opts = [str(a), str(a + 1), str(a - 1), str(a + 3)]
            explanation = f"{a * b} shared equally into groups of {b} gives {a} each."
        elif index % 4 == 2:
            q = f"Which is the same as {a} x 2?"
            answer = str(a * 2)
            opts = [str(a + 2), str(a * 2), str(a + a - 1), str(a * 3)]
            explanation = f"Doubling {a} gives {a * 2}."
        else:
            q = f"What is half of {a * 4}?"
            answer = str(a * 2)
            opts = [str(a * 2 - 1), str(a * 2), str(a * 2 + 1), str(a * 3)]
            explanation = f"Half of {a * 4} is {a * 2}."
    elif sec_id == 'fractions':
        half_num = base + 2
        if index % 4 == 0:
            q = f"What is 1/2 of {half_num * 2}?"
            answer = str(half_num)
            opts = [str(half_num - 1), str(half_num), str(half_num + 1), str(half_num + 3)]
            explanation = f"Half of {half_num * 2} is {half_num}."
        elif index % 4 == 1:
            q = f"Which fraction is equal to a quarter?"
            answer = '1/4'
            opts = ['1/2', '1/4', '3/4', '2/3']
            explanation = 'One quarter means one out of four equal parts.'
        elif index % 4 == 2:
            q = f"What is 1/4 of {base * 8}?"
            answer = str(base * 2)
            opts = [str(base), str(base * 2), str(base * 3), str(base * 4)]
            explanation = f"Divide {base * 8} by 4 to get {base * 2}."
        else:
            q = f"Which is larger: 1/2 or 1/4?"
            answer = '1/2'
            opts = ['1/4', '1/2', 'They are equal', 'Neither']
            explanation = 'Half is larger than a quarter when the whole is the same.'
    elif sec_id == 'money':
        p = base + 5
        if index % 4 == 0:
            q = f"What is {p}p + {base}p?"
            answer = str(p + base)
            opts = [str(p + base), str(p + base - 5), str(p + base + 10), str(p + base + 20)]
            explanation = f"{p}p plus {base}p makes {p + base}p."
        elif index % 4 == 1:
            q = f"What is £1 - {base}p?"
            answer = str(100 - base)
            opts = [str(100 - base), str(100 - base - 5), str(100 - base + 10), str(100 - base + 20)]
            explanation = f"£1 is 100p, so 100p - {base}p = {100 - base}p."
        elif index % 4 == 2:
            q = f"Which value is larger: {base}p or {base + 10}p?"
            answer = f'{base + 10}p'
            opts = [f'{base}p', f'{base + 10}p', 'They are equal', 'Neither']
            explanation = f"{base + 10}p is more than {base}p."
        else:
            q = f"What is {base + 20}p + {base + 5}p?"
            answer = str(base * 2 + 25)
            opts = [str(base * 2 + 20), str(base * 2 + 25), str(base * 2 + 30), str(base * 2 + 40)]
            explanation = f"Adding the amounts gives {base * 2 + 25}p."
    elif sec_id == 'time':
        hour = 1 + (index % 7)
        if index % 4 == 0:
            q = f"What is half past {hour}?"
            answer = f'{hour}:30'
            opts = [f'{hour}:00', f'{hour}:15', f'{hour}:30', f'{hour}:45']
            explanation = f"Half past {hour} is {hour}:30."
        elif index % 4 == 1:
            q = f"What is 15 minutes after {hour}:15?"
            answer = f'{hour}:30'
            opts = [f'{hour}:15', f'{hour}:30', f'{hour}:45', f'{hour + 1}:00']
            explanation = f"Add 15 minutes to {hour}:15 to make {hour}:30."
        elif index % 4 == 2:
            q = f"What is quarter to {hour + 1}?"
            answer = f'{hour}:45'
            opts = [f'{hour}:15', f'{hour}:30', f'{hour}:45', f'{hour + 1}:00']
            explanation = f"Quarter to {hour + 1} is {hour}:45."
        else:
            q = f"How many minutes are in {hour} hours?"
            answer = str(hour * 60)
            opts = [str(hour * 30), str(hour * 45), str(hour * 60), str(hour * 90)]
            explanation = f"Each hour has 60 minutes, so {hour} hours has {hour * 60} minutes."
    elif sec_id == 'geometry':
        if index % 4 == 0:
            q = "Which shape has 3 sides?"
            answer = 'Triangle'
            opts = ['Circle', 'Triangle', 'Square', 'Rectangle']
            explanation = 'A triangle has 3 sides.'
        elif index % 4 == 1:
            q = "Which solid shape is like a ball?"
            answer = 'Sphere'
            opts = ['Cube', 'Pyramid', 'Sphere', 'Cylinder']
            explanation = 'A sphere is round like a ball.'
        elif index % 4 == 2:
            q = 'How many corners does a square have?'
            answer = '4'
            opts = ['3', '4', '5', '6']
            explanation = 'A square has 4 corners.'
        else:
            q = 'Which shape has 4 equal sides?'
            answer = 'Square'
            opts = ['Triangle', 'Rectangle', 'Square', 'Circle']
            explanation = 'A square has 4 equal sides.'
    elif sec_id == 'position-direction':
        if index % 4 == 0:
            q = 'Which way is the opposite of left?'
            answer = 'Right'
            opts = ['North', 'Right', 'Down', 'Left']
            explanation = 'Right is the opposite of left.'
        elif index % 4 == 1:
            q = 'If you move 2 steps forward and then 1 step back, how many steps from the start?'
            answer = '1'
            opts = ['0', '1', '2', '3']
            explanation = '2 forward and 1 back leaves you 1 step in front of the start.'
        elif index % 4 == 2:
            q = 'A quarter turn is how many degrees?'
            answer = '90°'
            opts = ['45°', '90°', '180°', '360°']
            explanation = 'A quarter turn is 90 degrees.'
        else:
            q = 'Which direction is between north and east?'
            answer = 'North-east'
            opts = ['North-east', 'South-east', 'South-west', 'North-west']
            explanation = 'North-east is between north and east.'
    elif sec_id == 'measurement':
        if index % 4 == 0:
            q = f"Which is longer: {base} cm or {base + 15} cm?"
            answer = f'{base + 15} cm'
            opts = [f'{base} cm', f'{base + 15} cm', 'They are equal', 'Neither']
            explanation = f'{base + 15} cm is longer than {base} cm.'
        elif index % 4 == 1:
            q = f"What is {base * 10} g + {base * 5} g?"
            answer = str(base * 15)
            opts = [str(base * 10), str(base * 12), str(base * 15), str(base * 20)]
            explanation = f"{base * 10} g + {base * 5} g = {base * 15} g."
        elif index % 4 == 2:
            q = f"How many centimetres are in {base} metres?"
            answer = str(base * 100)
            opts = [str(base * 10), str(base * 50), str(base * 100), str(base * 500)]
            explanation = f"Each metre has 100 centimetres, so {base} metres is {base * 100} centimetres."
        else:
            q = f"What is {base * 2} ml + {base * 3} ml?"
            answer = str(base * 5)
            opts = [str(base * 4), str(base * 5), str(base * 6), str(base * 7)]
            explanation = f"{base * 2} ml + {base * 3} ml = {base * 5} ml."
    elif sec_id == 'statistics':
        if index % 4 == 0:
            q = f"A pictogram shows 3 symbols and each symbol is worth {base} apples. How many apples?"
            answer = str(base * 3)
            opts = [str(base * 2), str(base * 3), str(base * 4), str(base * 5)]
            explanation = f"3 symbols x {base} apples = {base * 3}."
        elif index % 4 == 1:
            q = f"Which total is greater: {base + 3} or {base + 8}?"
            answer = str(base + 8)
            opts = [str(base + 3), str(base + 8), 'They are equal', 'Neither']
            explanation = f"{base + 8} is greater than {base + 3}."
        elif index % 4 == 2:
            q = f"What is {base + 4} + {base + 2}?"
            answer = str((base + 4) + (base + 2))
            opts = [str((base + 4) + (base + 2) - 3), str((base + 4) + (base + 2)), str((base + 4) + (base + 2) + 2), str((base + 4) + (base + 2) + 10)]
            explanation = f"Adding the totals gives {(base + 4) + (base + 2)}."
        else:
            q = f"If 2 bars show {base} and {base + 2}, what is the difference?"
            answer = str(2)
            opts = ['1', '2', '3', '4']
            explanation = f"{base + 2} - {base} = 2."
    else:
        if index % 4 == 0:
            q = f"What is the next number in {base}, {base + 2}, {base + 4}, __?"
            answer = str(base + 6)
            opts = [str(base + 4), str(base + 5), str(base + 6), str(base + 8)]
            explanation = f"The pattern adds 2 each time, so the next is {base + 6}."
        elif index % 4 == 1:
            q = f"What is {base + 3} + {base + 1}?"
            answer = str((base + 3) + (base + 1))
            opts = [str((base + 3) + (base + 1) - 2), str((base + 3) + (base + 1)), str((base + 3) + (base + 1) + 2), str((base + 3) + (base + 1) + 5)]
            explanation = f"Adding the numbers gives {(base + 3) + (base + 1)}."
        elif index % 4 == 2:
            q = f"Which number is odd?"
            answer = str(base + 1)
            opts = [str(base), str(base + 1), str(base + 2), str(base + 4)]
            explanation = f"{base + 1} is odd because it ends in 1, 3, 5, 7 or 9."
        else:
            q = f"What is half of {base * 8}?"
            answer = str(base * 4)
            opts = [str(base * 3), str(base * 4), str(base * 5), str(base * 6)]
            explanation = f"Half of {base * 8} is {base * 4}."

    if difficulty == 'challenge':
        q += ' (challenge)'
    return {
        'id': f'{sec_id}-{index:02d}',
        'sectionId': sec_id,
        'sectionName': next(s['name'] for s in SECTIONS if s['id'] == sec_id),
        'skill': facts['skill'],
        'type': 'multiple-choice' if 'Q' not in locals() else 'multiple-choice',
        'difficulty': difficulty,
        'question': q,
        'options': opts,
        'correctAnswer': answer,
        'explanation': explanation,
        'hint': f'Use the {facts["example"]} idea to help.',
        'points': {'easy': 10, 'medium': 15, 'hard': 20, 'challenge': 25}[difficulty],
        'accessibilityDescription': q,
        'optionalEnrichment': difficulty == 'challenge',
    }

bank = []
seen = set()
for sec in SECTIONS:
    questions = []
    for idx, difficulty in enumerate(DIFFICULTY_ORDER, start=1):
        item = question_for(sec['id'], idx, difficulty)
        if item['id'] in seen:
            raise ValueError(f'duplicate id {item["id"]}')
        seen.add(item['id'])
        questions.append(item)
    bank.append({'id': sec['id'], 'name': sec['name'], 'world': sec['world'], 'icon': sec['icon'], 'introduction': sec['introduction'], 'objective': sec['objective'], 'questions': questions})

if len(bank) != 11:
    raise ValueError(f'Expected 11 sections, got {len(bank)}')
if sum(len(s['questions']) for s in bank) != 330:
    raise ValueError(f'Expected 330 questions, got {sum(len(s["questions"]) for s in bank)}')
OUT.write_text(json.dumps(bank, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'Created {OUT} with {sum(len(s["questions"]) for s in bank)} questions.')
