export interface ProgressState {
  completedSections: string[]
  bestScores: Record<string, number>
  totalStars: number
  lastPlayedAt: string | null
}

const STORAGE_KEY = 'maths-adventure-progress'

export const defaultProgress: ProgressState = {
  completedSections: [],
  bestScores: {},
  totalStars: 0,
  lastPlayedAt: null,
}

export function readProgress(): ProgressState {
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY)
    if (!raw) {
      return defaultProgress
    }

    const parsed = JSON.parse(raw) as Partial<ProgressState>
    return {
      ...defaultProgress,
      ...parsed,
      completedSections: Array.isArray(parsed.completedSections) ? parsed.completedSections : [],
      bestScores: parsed.bestScores && typeof parsed.bestScores === 'object' ? parsed.bestScores : {},
    }
  } catch {
    return defaultProgress
  }
}

export function saveProgress(progress: ProgressState) {
  window.localStorage.setItem(STORAGE_KEY, JSON.stringify(progress))
}

export function getSectionProgress(sectionId: string, progress: ProgressState) {
  return progress.completedSections.includes(sectionId)
}
