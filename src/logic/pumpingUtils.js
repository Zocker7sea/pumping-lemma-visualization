export function computeP(language) {
  if (language.isRegular) {
    return language.states;
  }

  return Math.floor(Math.random() * 20) + 1;
}

function randomUvLength(p) {
  // Gleichverteilte UV-Länge
  return Math.floor(Math.random() * p) + 1;
}

function getRandomDecomposition(word, p) {
  const uvLen = randomUvLength(p);

  // u zufällig, aber v mindestens 1
  const uLen = Math.floor(Math.random() * uvLen);
  const vLen = uvLen - uLen;
  if (vLen <= 0) return null;

  const u = word.slice(0, uLen);
  const v = word.slice(uLen, uLen + vLen);
  const w = word.slice(uLen + vLen);

  return { u, v, w };
}

export function getDecompositions(language, word, p) {
  if (!word || word.length < p) return [];

  // Reguläre Sprachen → kanonische Zerlegung
  if (
    language.isRegular &&
    typeof language.pumpingDecomposition === "function"
  ) {
    return [language.pumpingDecomposition(word, p)];
  }

  // Nicht-regulär → eine zufällige Dämon-Zerlegung
  const d = getRandomDecomposition(word, p);
  return d ? [d] : [];
}

export function pumpWord({ u, v, w }, i) {
  return u + v.repeat(i) + w;
}
