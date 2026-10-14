import { describe, expect, it } from 'vitest'
import { allQuestions, questionBank } from './questions'

describe('Maths Adventure question bank', () => {
  it('contains the full 11-section Year 2 bank', () => {
    expect(questionBank).toHaveLength(11)
    expect(allQuestions).toHaveLength(330)
  })

  it('matches the expected difficulty distribution', () => {
    const counts = allQuestions.reduce<Record<string, number>>((result, question) => {
      result[question.difficulty] = (result[question.difficulty] ?? 0) + 1
      return result
    }, {})

    expect(counts.easy).toBe(110)
    expect(counts.medium).toBe(110)
    expect(counts.hard).toBe(77)
    expect(counts.challenge).toBe(33)
  })
})
