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

//---------- Fehler Ausgabe ----------//
const errors = computed(() => {
  const e = []
  //Prüfe Wortlänge kleiner als P
  if (props.word.length < props.p) {
    e.push(`Wort muss mindestens ${props.p} Zeichen haben`)
  }
  //Prüfe ob Wort in Sprache liegt
  if (!props.language.isInLanguage(props.word)) {
    e.push("Wort liegt nicht in der Sprache")
  }
  return e
})

//---------- Gültigkeit des Wortes ----------//
const isValid = computed(() => errors.value.length === 0)
</script>

<template>
  <div class="space-y-4">
    <code class="text-lg ">Spieler wählt ein Wort w ∈ L | |w| ≥ {{p}}</code>

    <!-- Eingabefeld für Wort -->
    <input class="w-full border rounded px-3 py-2 mt-2" :value="word" @input="emit('update:word', $event.target.value)"
      placeholder="z. B. aabb" />

    <!-- Live Validator -->
    <div class="p-3 rounded text-sm" :class="isValid ? 'bg-green-50 text-green-700' : 'bg-red-50 text-red-700'">
      <ul v-if="errors.length">
        <li v-for="e in errors" :key="e">• {{ e }}</li>
      </ul>
      <p v-else>✓ Wort ist gültig</p>
    </div>

    <!-- Weiter Button -->
    <button class="px-4 py-2 rounded bg-red-700 w-full text-white disabled:opacity-50" :disabled="!isValid"
      @click="emit('next')">
      Weiter
    </button>
  </div>
</template>
