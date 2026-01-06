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
</script>

<template>
  <div class="space-y-4">
    <h2 class="text-xl font-semibold">Sprache auswählen</h2>

    <!-- Dropdown zur Sprachauswahl -->
    <select v-model="selectedLanguage" class="w-full text-xl border rounded px-3 py-2">
      <option disabled value="">Bitte Sprache wählen</option>
      <option v-for="lang in languages" :key="lang.id" :value="lang.id">
        {{ lang.label }} = {{ lang.name }}
      </option>
    </select>

    <!-- Anzeige der formalen Definition -->
    <div v-if="selectedLanguage" class="rounded border bg-gray-50 p-3 text-sm">
      <p class="font-medium text-xl">Formale Definition:</p>
      <p class="font-mono text-xl">
        {{ languageDefinitions[selectedLanguage].description }}
      </p>
    </div>

    <!-- Start Button -->
    <button v-if="selectedLanguage" class="px-4 py-2 rounded bg-blue-600 text-white"
      @click="emit('start', selectedLanguage)">
      Spiel starten
    </button>
  </div>
</template>
