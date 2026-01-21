<script setup>
//---------- Imports ---------- //
import { computed, ref } from "vue"
import { languageDefinitions } from "@/logic/languageDefinitions"

//---------- Emits ---------- //
const emit = defineEmits(["start"])

//---------- Reaktive Variablen ---------- //
const selectedLanguage = ref("")

//---------- Sortierung der Sprachen ---------- //
const languages = computed(() =>
  Object.values(languageDefinitions).sort((a, b) => a.order - b.order)
)
const examplesIn = computed(() =>
  languageDefinitions[selectedLanguage.value].examples.filter((w) => languageDefinitions[selectedLanguage.value].isInLanguage(w))
)

const examplesOut = computed(() =>
  languageDefinitions[selectedLanguage.value].examples.filter((w) => !languageDefinitions[selectedLanguage.value].isInLanguage(w))
)
</script>

<template>
  <div class="space-y-4">
    <!-- Dropdown zur Sprachauswahl -->
    <select v-model="selectedLanguage" class="w-full px-4 py-2 border-2 border-red-700 rounded
         focus:outline-none focus:ring-2 focus:ring-red-600
         bg-white text-gray-800
         hover:border-red-800">
      <option disabled value="">Bitte Sprache wählen</option>
      <option v-for="lang in languages" :key="lang.id" :value="lang.id">
        L{{ lang.order }} = {{ lang.name }}
      </option>
    </select>

    <!-- Anzeige der formalen Definition -->
    <div v-if="selectedLanguage" class="rounded border bg-gray-50 p-3 text-xl">
      <p class="font-medium">Formale Definition:</p>
      <p class="font-mono">
        {{ languageDefinitions[selectedLanguage].description }}
      </p>
      <p class="text-lg whitespace-pre-line">{{ languageDefinitions[selectedLanguage].info }}</p>
      <div class="mt-3 space-y-2">

  <!-- Wörter IN der Sprache -->
  <div v-if="examplesIn.length">
    <p class="text-sm font-semibold text-green-700">
      Wörter in der Sprache:
    </p>
    <div class="flex flex-wrap gap-2 mt-1">
      <span
        v-for="w in examplesIn"
        :key="w"
        class="px-2 py-1 rounded bg-green-200 text-green-900 font-mono text-sm"
      >
        {{ w === '' ? 'ε' : w }}
      </span>
    </div>
  </div>

  <!-- Wörter NICHT in der Sprache -->
  <div v-if="examplesOut.length">
    <p class="text-sm font-semibold text-red-700 mt-2">
      Wörter nicht in der Sprache:
    </p>
    <div class="flex flex-wrap gap-2 mt-1">
      <span
        v-for="w in examplesOut"
        :key="w"
        class="px-2 py-1 rounded bg-red-200 text-red-900 font-mono text-sm"
      >
        {{ w === '' ? 'ε' : w }}
      </span>
    </div>
  </div>

</div>

    </div>

    <!-- Start Button -->
    <button v-if="selectedLanguage" class="w-full px-4 py-2 rounded bg-red-700 text-white"
      @click="emit('start', selectedLanguage)" aria-label="Mit ausgewählter Sprache starten">
      <p class="font-bold">Spiel mit dieser Sprache starten </p>
    </button>
  </div>
</template>
