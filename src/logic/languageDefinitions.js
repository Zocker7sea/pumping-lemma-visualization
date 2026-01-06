export const languageDefinitions = {
  anbn: {
    order: 1,
    id: "anbn",
    label: "L1",
    name: "aⁿbⁿ",
    description: "L = { aⁿ bⁿ | n ≥ 0 }",
    alphabet: ["a", "b"],

    isInLanguage(word) {
      const match = word.match(/^(a+)(b+)$/)
      return match && match[1].length === match[2].length
    }
  },

  anbm: {
    order: 2,
    id: "anbm",
    label: "L2",
    name: "aⁿbᵐ",
    description: "L = { aⁿ bᵐ | n, m ≥ 0 }",
    alphabet: ["a", "b"],

    isInLanguage(word) {
      return /^[ab]*$/.test(word)
    }
  }
}
