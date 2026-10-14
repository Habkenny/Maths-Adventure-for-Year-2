import { useMemo, useState } from 'react'
import './App.css'
import { questionBank } from './data/questions'
import { readProgress, saveProgress, type ProgressState } from './lib/storage'

type Screen = 'home' | 'quiz' | 'results'
type Feedback = { correct: boolean; message: string }

function App() {
  const [screen, setScreen] = useState<Screen>('home')
  const [selectedSectionId, setSelectedSectionId] = useState<string | null>(null)
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0)
  const [answers, setAnswers] = useState<Record<string, string | number | boolean>>({})
  const [score, setScore] = useState(0)
  const [feedback, setFeedback] = useState<Feedback | null>(null)
  const [showHint, setShowHint] = useState(false)
  const [locked, setLocked] = useState(false)
  const [progress, setProgress] = useState<ProgressState>(() => readProgress())

  const selectedSection = useMemo(
    () => questionBank.find((section) => section.id === selectedSectionId) ?? null,
    [selectedSectionId],
  )

  const currentQuestion = selectedSection?.questions[currentQuestionIndex] ?? null

  const startSection = (sectionId: string) => {
    setSelectedSectionId(sectionId)
    setCurrentQuestionIndex(0)
    setAnswers({})
    setScore(0)
    setFeedback(null)
    setShowHint(false)
    setLocked(false)
    setScreen('quiz')
  }

  const finishSection = (finalScore: number) => {
    const section = selectedSection
    if (!section) {
      setScreen('home')
      return
    }

    const updatedBestScores = {
      ...progress.bestScores,
      [section.id]: Math.max(progress.bestScores[section.id] ?? 0, finalScore),
    }

    const totalStars = Object.values(updatedBestScores).reduce(
      (sum, value) => sum + Math.max(0, Math.round(value / 100)),
      0,
    )

    const nextProgress: ProgressState = {
      ...progress,
      completedSections: Array.from(new Set([...progress.completedSections, section.id])),
      bestScores: updatedBestScores,
      totalStars,
      lastPlayedAt: new Date().toISOString(),
    }

    setProgress(nextProgress)
    saveProgress(nextProgress)
    setScreen('results')
  }

  const submitAnswer = (value: string | number | boolean) => {
    if (!currentQuestion || locked) {
      return
    }

    setLocked(true)

    const nextAnswers = { ...answers, [currentQuestion.id]: value }
    setAnswers(nextAnswers)

    const isCorrect = value === currentQuestion.correctAnswer
    const earnedPoints = isCorrect ? currentQuestion.points : 0
    const nextScore = score + earnedPoints
    setScore(nextScore)

    setFeedback({
      correct: isCorrect,
      message: isCorrect
        ? `Correct! ${currentQuestion.explanation}`
        : `Not quite this time. ${currentQuestion.explanation}`,
    })

    const nextIndex = currentQuestionIndex + 1
    const totalQuestions = selectedSection?.questions.length ?? 0

    window.setTimeout(() => {
      if (nextIndex >= totalQuestions) {
        finishSection(nextScore)
        return
      }

      setCurrentQuestionIndex(nextIndex)
      setFeedback(null)
      setShowHint(false)
      setLocked(false)
    }, 900)
  }

  const resetToHome = () => {
    setScreen('home')
    setSelectedSectionId(null)
    setCurrentQuestionIndex(0)
    setAnswers({})
    setScore(0)
    setFeedback(null)
    setShowHint(false)
    setLocked(false)
  }

  const totalPossible = selectedSection?.questions.reduce((sum, question) => sum + question.points, 0) ?? 0
  const percentage = totalPossible > 0 ? Math.round((score / totalPossible) * 100) : 0

  return (
    <div className="app-shell">
      <header className="topbar">
        <button type="button" className="brand" onClick={resetToHome}>
          <span className="brand-icon">✨</span>
          Maths Adventure
        </button>
        <div className="topbar-meta">
          <span>{progress.completedSections.length} worlds cleared</span>
          <span>{progress.totalStars} stars</span>
        </div>
      </header>

      {screen === 'home' && (
        <main className="home-screen">
          <section className="hero-panel">
            <div>
              <p className="eyebrow">Year 2 adventure</p>
              <h1>Learn maths through magical missions.</h1>
              <p className="lead">
                Explore each world, build confidence, and become a maths champion.
              </p>
            </div>
            <div className="hero-card">
              <div className="hero-stat">
                <strong>{questionBank.length}</strong>
                <span>sections</span>
              </div>
              <div className="hero-stat">
                <strong>{questionBank.reduce((count, section) => count + section.questions.length, 0)}</strong>
                <span>questions</span>
              </div>
            </div>
          </section>

          <section className="section-grid" aria-label="Math worlds">
            {questionBank.map((section) => {
              const bestScore = progress.bestScores[section.id] ?? 0
              const isCompleted = progress.completedSections.includes(section.id)

              return (
                <article key={section.id} className="section-card">
                  <div className="card-head">
                    <span className="world-icon" aria-hidden="true">{section.icon}</span>
                    <span className="badge">{section.world}</span>
                  </div>
                  <h2>{section.title}</h2>
                  <p>{section.introduction}</p>
                  <ul>
                    <li>{section.questions.length} questions</li>
                    <li>{isCompleted ? 'Completed' : 'Ready to play'}</li>
                    <li>Best score: {bestScore}</li>
                  </ul>
                  <button type="button" onClick={() => startSection(section.id)}>
                    {isCompleted ? 'Play again' : 'Start mission'}
                  </button>
                </article>
              )
            })}
          </section>
        </main>
      )}

      {screen === 'quiz' && selectedSection && currentQuestion && (
        <main className="quiz-screen">
          <div className="quiz-header">
            <div>
              <p className="eyebrow">{selectedSection.world}</p>
              <h2>{selectedSection.title}</h2>
            </div>
            <div className="question-progress">
              Question {currentQuestionIndex + 1} / {selectedSection.questions.length}
            </div>
          </div>

          <div className="question-card">
            <div className="difficulty-pill">{currentQuestion.difficulty}</div>
            <h3>{currentQuestion.question}</h3>

            {currentQuestion.type === 'fill-in' ? (
              <div className="input-area">
                <label htmlFor="answer-input" className="sr-only">
                  Type your answer
                </label>
                <input
                  id="answer-input"
                  type="number"
                  placeholder="Type your answer"
                  disabled={locked}
                  onKeyDown={(event) => {
                    if (event.key === 'Enter') {
                      const target = event.target as HTMLInputElement
                      const value = Number(target.value)
                      if (target.value.trim() !== '') {
                        submitAnswer(value)
                        target.value = ''
                      }
                    }
                  }}
                />
                <button type="button" disabled={locked} onClick={() => {
                  const input = document.getElementById('answer-input') as HTMLInputElement | null
                  if (!input || input.value.trim() === '') return
                  submitAnswer(Number(input.value))
                  input.value = ''
                }}>
                  Check answer
                </button>
              </div>
            ) : (
              <div className="answer-grid" role="list">
                {(currentQuestion.options ?? []).map((option) => (
                  <button
                    key={String(option)}
                    type="button"
                    className="answer-option"
                    disabled={locked}
                    onClick={() => submitAnswer(option)}
                  >
                    {String(option)}
                  </button>
                ))}
              </div>
            )}

            <div className="question-meta">
              <span>Skill: {currentQuestion.skill}</span>
              <span>+{currentQuestion.points} pts</span>
            </div>

            {feedback && (
              <div className={`feedback ${feedback.correct ? 'correct' : 'incorrect'}`}>
                <strong>{feedback.correct ? 'Correct!' : 'Almost there!'}</strong>
                <p>{feedback.message}</p>
                {!showHint ? (
                  <button type="button" className="secondary-button" onClick={() => setShowHint(true)}>
                    Reveal hint
                  </button>
                ) : (
                  <p className="hint-box">Hint: {currentQuestion.hint}</p>
                )}
              </div>
            )}
          </div>
        </main>
      )}

      {screen === 'results' && selectedSection && (
        <main className="results-screen">
          <div className="results-card">
            <p className="eyebrow">Mission complete</p>
            <h2>{selectedSection.title}</h2>
            <div className="score-ring">
              <strong>{percentage}%</strong>
            </div>
            <p className="result-line">
              You scored {score} points out of {totalPossible}.
            </p>
            <div className="results-actions">
              <button type="button" onClick={() => startSection(selectedSection.id)}>
                Try again
              </button>
              <button type="button" className="secondary" onClick={resetToHome}>
                Back to worlds
              </button>
            </div>
          </div>
        </main>
      )}
    </div>
  )
}

export default App
