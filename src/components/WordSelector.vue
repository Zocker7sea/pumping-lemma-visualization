<script setup>
//---------- Imports ----------//
import { computed } from "vue"

//---------- Props ----------//
const props = defineProps({
  language: Object,
  p: Number,
  word: String
})
//---------- Emits ----------//
const emit = defineEmits(["update:word", "next"])

//---------- BASIS-FEHLER ----------//
function basicWordError(word) {
  if (!word) return "Bitte gib ein Wort ein."
  if (!/^[abc]*$/.test(word)) return "Das Wort enthält ungültige Zeichen."
  return ""
}

//---------- SPRACHSPEZIFISCHE ERKLÄRUNG ----------//
function explainWhyNot(language, word) {
  switch (language.id) {
    case "anbn":
      return "Die Anzahl der a und b ist nicht gleich oder die Reihenfolge ist falsch."

    case "evena":
      return "Die Anzahl der a ist ungerade."

    case "abab":
      return "Das Wort besteht nicht aus vollständigen „ab“-Blöcken."

    case "anbncn":
      return "Die Anzahl von a, b und c ist nicht gleich oder die Reihenfolge stimmt nicht."

    case "palindrome":
      return "Das Wort ist vorwärts und rückwärts nicht gleich."

    case "astar":
      return "Das Wort enthält andere Zeichen als „a“."

    case "anbman":
      return "Die Anzahl der a am Anfang und am Ende ist nicht gleich."

    case "ak2":
      return "Die Wortlänge ist kein Quadrat."

    case "anbm_n_greater_m":
      return "Die Anzahl der a ist nicht strikt größer als die Anzahl der b."

    default:
      return "Das Wort erfüllt die Bedingungen der Sprache nicht."
  }
}

//---------- ZENTRALE FEHLERMELDUNG ----------//
const errorMessage = computed(() => {
  // 1. leeres Wort
  if (!props.word) return "Bitte gib ein Wort ein."

  // 2. Alphabet-Check (NEU & WICHTIG)
  const alphaError = alphabetError(props.language, props.word)
  if (alphaError) return alphaError

  // 3. Pumping-Lemma-Bedingung
  if (props.word.length < props.p) {
    return `Wort muss mindestens ${props.p} Zeichen haben.`
  }

  // 4. Sprachspezifische Bedingung
  if (!props.language.isInLanguage(props.word)) {
    return explainWhyNot(props.language, props.word)
  }

  return ""
})
//---------- ALPHABET-ÜBERPRÜFUNG ----------//
function alphabetError(language, word) {
  for (const c of word) {
    if (!language.alphabet.includes(c)) {
      return `Ungültiges Zeichen '${c}'. Erlaubt sind nur: ${language.alphabet.join(
        ", "
      )}.`
    }
  }
  return ""
}

//---------- Gültigkeit des Wortes ----------//
const isValid = computed(() => errorMessage.value === "")
</script>

<template>
  <div class="space-y-4">
    <code class="text-lg ">Spieler wählt ein Wort w ∈ L | |w| ≥ {{ p }}</code>

    <!-- Eingabefeld für Wort -->
    <input class="w-full border rounded px-3 py-2 mt-2" :value="word" @input="emit('update:word', $event.target.value)"
      placeholder="z. B. aabb" />

    <!-- Fehlermeldung -->
    <p v-if="errorMessage" class="text-red-600 text-sm">
      {{ errorMessage }}
    </p>

    <!-- Weiter Button -->
    <button class="px-4 py-2 rounded bg-red-700 w-full text-white disabled:opacity-50" :disabled="!isValid"
      @click="emit('next')">
      Wort festlegen
    </button>
  </div>
</template>
