export const languageDefinitions = {
  anbn: {
    order: 1,
    id: "anbn",
    label: "L1",
    name: "aⁿbⁿ",
    description: "L = { aⁿ bⁿ | n ≥ 0 }",
    info: "In dieser Sprache stehen gleich viele a wie b, wobei zuerst alle a und danach alle b kommen.",
    alphabet: ["a", "b"],
    isRegular: false,
    states: null,

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
    info: "Diese Sprache erlaubt beliebig viele a gefolgt von beliebig vielen b. Die Anzahl ist unabhängig.",
    alphabet: ["a", "b"],
    isRegular: false,
    states: null,

    isInLanguage(word) {
      return /^[ab]*$/.test(word)
    }
  },

  abab: {
    order: 3,
    id: "abab",
    label: "L3",
    name: "(ab)*",
    description: "L = { (ab)ⁿ | n ≥ 0 }",
    info: "Diese Sprache besteht aus beliebig vielen Wiederholungen des Musters „ab“.",
    alphabet: ["a", "b"],
    isRegular: true,
    states: 2,

    isInLanguage(word) {
      return /^(ab)*$/.test(word)
    }
  }
}
