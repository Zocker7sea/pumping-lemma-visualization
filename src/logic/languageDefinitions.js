export const languageDefinitions = {
  anbn: {
    order: 1,
    id: "anbn",
    label: "L1",
    name: "aⁿbⁿ",
    description: "L = { aⁿ bⁿ | n ≥ 0 }",
    info: `
Diese Sprache enthält alle Wörter, die aus gleich vielen a wie b bestehen.
Dabei kommen zuerst alle a und danach alle b.
`,
    examples: ["", "ab", "aabb", "aba", "aabbb"],
    alphabet: ["a", "b"],
    isRegular: false,
    states: null,

    isInLanguage(word) {
      const match = word.match(/^(a+)(b+)$/);
      return match && match[1].length === match[2].length;
    },
  },

  evena: {
    order: 2,
    id: "evena",
    label: "L2",
    name: "gerade Anzahl von a",
    description: "L = { w ∈ {a,b}* | Anzahl(a) ist gerade }",
    info: `
Diese Sprache enthält genau die Wörter über {a,b},
in denen die Anzahl der a gerade ist.
`,
    examples: ["", "bb", "aabb", "a", "aba"],
    alphabet: ["a", "b"],
    isRegular: true,
    states: 2,

    isInLanguage(word) {
      let count = 0;
      for (const c of word) {
        if (c === "a") count++;
        else if (c !== "b") return false;
      }
      return count % 2 === 0;
    },

    pumpingDecomposition(word, p) {
      return {
        u: "",
        v: word.slice(0, 1),
        w: word.slice(1),
      };
    },
  },

  abab: {
    order: 3,
    id: "abab",
    label: "L3",
    name: "(ab)*",
    description: "L = { (ab)ⁿ | n ≥ 0 }",
    info: `
Diese Sprache besteht aus beliebig vielen Wiederholungen
des Musters „ab“.
`,
    examples: ["", "ab", "abab", "aba", "aabb"],
    alphabet: ["a", "b"],
    isRegular: true,
    states: 2,

    isInLanguage(word) {
      return /^(ab)*$/.test(word);
    },

    pumpingDecomposition(word, p) {
      return {
        u: "",
        v: word.slice(0, p),
        w: word.slice(p),
      };
    },
  },

  anbncn: {
    order: 4,
    id: "anbncn",
    label: "L4",
    name: "aⁿbⁿcⁿ",
    description: "L = { aⁿ bⁿ cⁿ | n ≥ 0 }",
    info: `
Diese Sprache enthält Wörter mit gleich vielen a, b und c
in genau dieser Reihenfolge.
`,
    examples: ["", "abc", "aabbcc", "abcc", "aabbc"],
    alphabet: ["a", "b", "c"],
    isRegular: false,
    states: null,

    isInLanguage(word) {
      const match = word.match(/^(a+)(b+)(c+)$/);
      return (
        match &&
        match[1].length === match[2].length &&
        match[2].length === match[3].length
      );
    },
  },

  palindrome: {
    order: 5,
    id: "palindrome",
    label: "L5",
    name: "Palindrome",
    description: "L = { w ∈ {a,b}* | w = wᴿ }",
    info: `
Diese Sprache enthält alle Wörter,
die vorwärts und rückwärts gleich sind.
`,
    examples: ["", "aba", "abba", "ab", "aabb"],
    alphabet: ["a", "b"],
    isRegular: false,
    states: null,

    isInLanguage(word) {
      return word === word.split("").reverse().join("");
    },
  },

  astar: {
    order: 6,
    id: "astar",
    label: "L6",
    name: "a*",
    description: "L = { aⁿ | n ≥ 0 }",
    info: `
Diese Sprache enthält beliebig viele a,
auch das leere Wort.
`,
    examples: ["", "a", "aaaa", "b", "ab"],
    alphabet: ["a"],
    isRegular: true,
    states: 1,

    isInLanguage(word) {
      return /^a*$/.test(word);
    },

    pumpingDecomposition(word, p) {
      return {
        u: "",
        v: word.slice(0, p),
        w: word.slice(p),
      };
    },
  },

  anbman: {
    order: 7,
    id: "anbman",
    label: "L7",
    name: "aⁿbᵐaⁿ",
    description: "L = { aⁿ bᵐ aⁿ | n, m ≥ 0 }",
    info: `
Diese Sprache verlangt gleich viele a
am Anfang und am Ende des Wortes.
Dazwischen dürfen beliebig viele b stehen.
`,
    examples: ["", "aba", "aabbaa", "abaa", "aabba"],
    alphabet: ["a", "b"],
    isRegular: false,
    states: null,

    isInLanguage(word) {
      const match = word.match(/^(a+)(b*)(a+)$/);
      return match && match[1].length === match[3].length;
    },
  },

  ak2: {
    order: 8,
    id: "ak2",
    label: "L8",
    name: "aᵏ²",
    description: "L = { a^{k²} | k ≥ 0 }",
    info: `
Diese Sprache enthält genau die Wörter,
deren Länge ein Quadrat ist.
`,
    examples: ["", "a", "aaaa", "aa", "aaaaa"],
    alphabet: ["a"],
    isRegular: false,
    states: null,

    isInLanguage(word) {
      if (!/^a*$/.test(word)) return false;
      const len = word.length;
      const k = Math.floor(Math.sqrt(len));
      return k * k === len;
    },
  },

  anbm_n_greater_m: {
    order: 9,
    id: "anbm_n_greater_m",
    label: "L9",
    name: "aⁿbᵐ mit n > m",
    description: "L = { aⁿ bᵐ | n > m }",
    info: `
Diese Sprache enthält Wörter mit mehr a als b.
Dabei stehen alle a vor allen b.
`,
    examples: ["a", "aab", "aaabb", "ab", "aabb"],
    alphabet: ["a", "b"],
    isRegular: false,
    states: null,

    isInLanguage(word) {
      const match = word.match(/^(a*)(b*)$/);
      if (!match) return false;
      return match[1].length > match[2].length;
    },
  },
};
