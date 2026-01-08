export function computeP(language) {
  if (language.isRegular) {
    return language.states
  }

  return Math.floor(Math.random() * 20) + 1
}
