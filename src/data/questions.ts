export type Difficulty = 'easy' | 'medium' | 'hard' | 'challenge'
export type QuestionType = 'multiple-choice' | 'fill-in' | 'true-false' | 'word-problem'

export interface Question {
  id: string
  sectionId: string
  sectionName: string
  skill: string
  type: QuestionType
  difficulty: Difficulty
  question: string
  options?: Array<string | number | boolean>
  correctAnswer: string | number | boolean
  explanation: string
  hint: string
  points: number
  accessibilityDescription?: string
  optionalEnrichment?: boolean
}

export interface Section {
  id: string
  title: string
  world: string
  icon: string
  introduction: string
  objective: string
  questions: Question[]
}

const difficultyOrder: Difficulty[] = [
  'easy',
  'easy',
  'easy',
  'easy',
  'easy',
  'easy',
  'easy',
  'easy',
  'easy',
  'easy',
  'medium',
  'medium',
  'medium',
  'medium',
  'medium',
  'medium',
  'medium',
  'medium',
  'medium',
  'medium',
  'hard',
  'hard',
  'hard',
  'hard',
  'hard',
  'hard',
  'hard',
  'challenge',
  'challenge',
  'challenge',
]

const sectionBlueprints = [
  {
    id: 'number-place-value',
    title: 'Number and Place Value',
    world: 'Number Jungle',
    icon: '🌿',
    introduction: 'Explore tens, ones and number patterns in the jungle.',
    objective: 'Understand numbers up to 100 and compare them efficiently.',
  },
  {
    id: 'addition-subtraction',
    title: 'Addition and Subtraction',
    world: 'Addition Island',
    icon: '🏝️',
    introduction: 'Use number bonds and mental maths on the island.',
    objective: 'Solve addition and subtraction questions with confidence.',
  },
  {
    id: 'multiplication-division',
    title: 'Multiplication and Division',
    world: 'Multiplication Mountain',
    icon: '⛰️',
    introduction: 'Group objects and share equally on the mountain trail.',
    objective: 'Use equal groups, arrays and sharing strategies.',
  },
  {
    id: 'fractions',
    title: 'Fractions',
    world: 'Fraction Forest',
    icon: '🌲',
    introduction: 'Find halves and quarters in the forest.',
    objective: 'Recognise and compare simple fractions of shapes and amounts.',
  },
  {
    id: 'money',
    title: 'Money',
    world: 'Money Market',
    icon: '🪙',
    introduction: 'Count coins and notes in the busy market.',
    objective: 'Work with totals and simple change in everyday context.',
  },
  {
    id: 'time',
    title: 'Time',
    world: 'Time Traveller Town',
    icon: '🕒',
    introduction: 'Read clocks and times of day in the town square.',
    objective: 'Tell the time to o’clock, half past and quarter past/to.',
  },
  {
    id: 'geometry',
    title: 'Geometry — 2D and 3D Shapes',
    world: 'Shape Space',
    icon: '🧩',
    introduction: 'Spot shapes and properties all around space.',
    objective: 'Identify 2D and 3D shapes and describe their features.',
  },
  {
    id: 'position-direction',
    title: 'Position, Direction and Movement',
    world: 'Direction Maze',
    icon: '🧭',
    introduction: 'Follow directions and learn movement in a maze.',
    objective: 'Use positional and directional language accurately.',
  },
  {
    id: 'measurement',
    title: 'Measurement',
    world: 'Measurement Lab',
    icon: '📏',
    introduction: 'Measure objects and compare lengths, mass and volume.',
    objective: 'Choose suitable units and compare measures effectively.',
  },
  {
    id: 'statistics',
    title: 'Statistics and Data Handling',
    world: 'Data Detective Club',
    icon: '📊',
    introduction: 'Read pictograms and simple charts to solve mysteries.',
    objective: 'Interpret and compare data using tables and charts.',
  },
  {
    id: 'reasoning',
    title: 'Problem-Solving and Mathematical Reasoning',
    world: 'Puzzle Kingdom',
    icon: '👑',
    introduction: 'Use brave thinking to solve puzzle problems.',
    objective: 'Apply logic and multi-step maths to solve challenges.',
  },
] as const

const pointsByDifficulty: Record<Difficulty, number> = {
  easy: 10,
  medium: 15,
  hard: 20,
  challenge: 25,
}

function buildQuestion(sectionId: string, sectionName: string, questionNumber: number, difficulty: Difficulty): Question {
  const skillMap: Record<string, string> = {
    'number-place-value': 'place value',
    'addition-subtraction': 'number bonds',
    'multiplication-division': 'equal groups',
    fractions: 'fractions',
    money: 'money',
    time: 'time',
    geometry: 'shapes',
    'position-direction': 'direction',
    measurement: 'measurement',
    statistics: 'data',
    reasoning: 'reasoning',
  }

  const base = questionNumber * 3 + 4
  const points = pointsByDifficulty[difficulty]
  const skill = skillMap[sectionId] ?? 'maths'

  switch (sectionId) {
    case 'number-place-value': {
      const value = base + 12
      const subtract = base + 5
      return {
        id: `${sectionId}-${questionNumber}`,
        sectionId,
        sectionName,
        skill,
        type: 'multiple-choice',
        difficulty,
        question: `What is ${value} - ${subtract}?`,
        options: [String(value - subtract), String(value - subtract + 3), String(value - subtract + 7), String(value - subtract - 2)],
        correctAnswer: String(value - subtract),
        explanation: `${value} minus ${subtract} is ${value - subtract}.`,
        hint: 'Count back carefully.',
        points,
        accessibilityDescription: 'Subtracting numbers',
      }
    }
    case 'addition-subtraction': {
      const left = base + 7
      const right = base
      const total = left + right
      return {
        id: `${sectionId}-${questionNumber}`,
        sectionId,
        sectionName,
        skill,
        type: 'multiple-choice',
        difficulty,
        question: `What is ${left} + ${right}?`,
        options: [String(total), String(total - 2), String(total + 4), String(total + 9)],
        correctAnswer: String(total),
        explanation: `${left} plus ${right} makes ${total}.`,
        hint: 'Add the tens and ones carefully.',
        points,
        accessibilityDescription: 'Addition question',
      }
    }
    case 'multiplication-division': {
      const value = base + 1
      const answer = value * 2
      return {
        id: `${sectionId}-${questionNumber}`,
        sectionId,
        sectionName,
        skill,
        type: 'fill-in',
        difficulty,
        question: `What is ${value} x 2?`,
        correctAnswer: answer,
        explanation: `${value} doubled is ${answer}.`,
        hint: 'Double the number.',
        points,
      }
    }
    case 'fractions': {
      const whole = base * 4
      const half = whole / 2
      return {
        id: `${sectionId}-${questionNumber}`,
        sectionId,
        sectionName,
        skill,
        type: 'multiple-choice',
        difficulty,
        question: `What is one half of ${whole}?`,
        options: [String(half), String(half - 2), String(half + 2), String(whole)],
        correctAnswer: String(half),
        explanation: `Half of ${whole} is ${half}.`,
        hint: 'Split into 2 equal groups.',
        points,
      }
    }
    case 'money': {
      const coin1 = base + 5
      const coin2 = base + 12
      const total = coin1 + coin2
      return {
        id: `${sectionId}-${questionNumber}`,
        sectionId,
        sectionName,
        skill,
        type: 'multiple-choice',
        difficulty,
        question: `What is ${coin1}p + ${coin2}p?`,
        options: [String(total), String(total - 5), String(total + 5), String(total + 20)],
        correctAnswer: String(total),
        explanation: `${coin1}p plus ${coin2}p makes ${total}p.`,
        hint: 'Add the pence together.',
        points,
      }
    }
    case 'time': {
      const hour = ((base + 1) % 12) + 1
      return {
        id: `${sectionId}-${questionNumber}`,
        sectionId,
        sectionName,
        skill,
        type: 'multiple-choice',
        difficulty,
        question: `What is half past ${hour}?`,
        options: [`${hour}:00`, `${hour}:15`, `${hour}:30`, `${hour}:45`],
        correctAnswer: `${hour}:30`,
        explanation: `Half past ${hour} is ${hour}:30.`,
        hint: 'The minute hand is on 6.',
        points,
      }
    }
    case 'geometry': {
      return {
        id: `${sectionId}-${questionNumber}`,
        sectionId,
        sectionName,
        skill,
        type: 'true-false',
        difficulty,
        question: 'A triangle has three sides.',
        options: ['True', 'False'],
        correctAnswer: true,
        explanation: 'A triangle has three sides.',
        hint: 'Count the sides.',
        points,
      }
    }
    case 'position-direction': {
      return {
        id: `${sectionId}-${questionNumber}`,
        sectionId,
        sectionName,
        skill,
        type: 'multiple-choice',
        difficulty,
        question: 'Which way is the opposite of left?',
        options: ['North', 'Right', 'Down', 'Left'],
        correctAnswer: 'Right',
        explanation: 'Right is the opposite of left.',
        hint: 'Think of turning around.',
        points,
      }
    }
    case 'measurement': {
      const first = base
      const second = base + 12
      return {
        id: `${sectionId}-${questionNumber}`,
        sectionId,
        sectionName,
        skill,
        type: 'multiple-choice',
        difficulty,
        question: `Which is longer: ${first} cm or ${second} cm?`,
        options: [`${first} cm`, `${second} cm`, 'They are the same', 'Neither'],
        correctAnswer: `${second} cm`,
        explanation: `${second} cm is longer than ${first} cm.`,
        hint: 'Compare the numbers.',
        points,
      }
    }
    case 'statistics': {
      const start = base
      const end = base + 3
      return {
        id: `${sectionId}-${questionNumber}`,
        sectionId,
        sectionName,
        skill,
        type: 'word-problem',
        difficulty,
        question: `If two bars show ${start} and ${end}, what is the difference?`,
        options: ['2', '3', '4', '5'],
        correctAnswer: '3',
        explanation: `${end} minus ${start} is 3.`,
        hint: 'Find the gap between the values.',
        points,
      }
    }
    case 'reasoning': {
      const startValue = base
      const nextValue = startValue + 2
      return {
        id: `${sectionId}-${questionNumber}`,
        sectionId,
        sectionName,
        skill,
        type: 'multiple-choice',
        difficulty,
        question: `What comes next: ${startValue}, ${nextValue}, ${startValue + 4}, __?`,
        options: [String(startValue + 5), String(startValue + 6), String(startValue + 7), String(startValue + 8)],
        correctAnswer: String(startValue + 6),
        explanation: 'The pattern increases by 2 each time, so the next number is ' + String(startValue + 6) + '.',
        hint: 'Look for the number pattern.',
        points,
      }
    }
    default:
      return {
        id: `${sectionId}-${questionNumber}`,
        sectionId,
        sectionName,
        skill,
        type: 'multiple-choice',
        difficulty,
        question: 'Choose the correct answer.',
        options: ['1', '2', '3', '4'],
        correctAnswer: '1',
        explanation: 'This is a sample question.',
        hint: 'Check each option carefully.',
        points,
      }
  }
}

export const questionBank: Section[] = sectionBlueprints.map((section) => ({
  ...section,
  questions: Array.from({ length: 30 }, (_, index) => {
    const difficulty = difficultyOrder[index]
    return buildQuestion(section.id, section.title, index + 1, difficulty)
  }),
}))

export const allQuestions = questionBank.flatMap((section) => section.questions)

export default questionBank
