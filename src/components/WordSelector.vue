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

//---------- ZENTRALE FEHLERMELDUNG ----------//
const errorMessage = computed(() => {
  // 1. leeres Wort
  if (!props.word) return "Bitte gib ein Wort ein."

  // 2. Pumping-Lemma-Bedingung
  if (props.word.length < props.p) {
    return `Wort muss mindestens ${props.p} Zeichen haben.`
  }

  // 3. Sprachspezifische Bedingung
  if (!props.language.isInLanguage(props.word)) {
    return props.language.errors?.(props.word)[0]
}

  return ""
})

//---------- Gültigkeit des Wortes ----------//
const isValid = computed(() => errorMessage.value === "")
</script>

<template>
  <div class="space-y-4">
    <code class="text-lg ">Spieler wählt ein Wort w ∈ L | |w| ≥ {{ p }}</code>

    <!-- Eingabefeld für Wort -->
    <input class="w-full border rounded px-3 py-2 mt-2"
    :class="{
    'border-green-500 bg-green-100 focus:ring-green-400': isValid,
    'border-red-300 bg-red-100': !isValid
  }"
    :value="word" @input="emit('update:word', $event.target.value)"
      placeholder="z. B. aabb" />

    <!-- Fehlermeldung -->
    <p v-if="errorMessage" class="text-red-600 text-sm">
      {{ errorMessage }}
    </p>
    <p
      v-if="isValid"
      class="mt-1 text-sm text-green-600 flex items-center gap-1"
    >
      <span>✔</span>
      <span>Das Wort gehört zur Sprache.</span>
    </p>

    <!-- Weiter Button -->
    <button class="px-4 py-2 rounded bg-red-700 w-full text-white disabled:opacity-50" :disabled="!isValid"
      @click="emit('next')" aria-label="Wort festlegen und zum nächsten Schritt">
      Wort festlegen
    </button>
  </div>
</template>
