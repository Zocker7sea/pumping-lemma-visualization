<script setup>
import { ref, computed, watch } from "vue"
import { languageDefinitions } from "@/logic/languageDefinitions"
import { computeP } from "@/logic/pumpingUtils"
import { useRouter } from "vue-router"


//---------- Komponenten ---------- //
import LanguageSelector from "@/components/LanguageSelector.vue"
import WordSelector from "@/components/WordSelector.vue"
import DecompositionView from "@/components/DecompositionView.vue"
import PumpFactorSelector from "@/components/PumpFactorSelector.vue"


//---------- Spielzustände ---------- //
const Step = {
  LANGUAGE: 0,
  WORD_SELECT: 1,
  DECOMPOSE: 2,
  PUMP: 3
}

//---------- Reaktive Variablen ---------- //
const currentStep = ref(Step.LANGUAGE) // Aktueller Schritt
const history = ref([]) // Verlauf der Schritte
const selectedLanguage = ref(null) // Ausgewählte Sprache
const p = ref(null) // Pumping-Länge   
const word = ref("") // Gewähltes Wort
const i = ref(1) // Pumpfaktor
const router = useRouter()

//---------- Dämon P Wert ---------- //
function demonChoosesP() {
  const language = languageDefinitions[selectedLanguage.value]
  p.value = computeP(language)
}

//---------- Zerlegung uvw ---------- //
const u = computed(() => word.value.slice(0, p.value - 1))
const v = computed(() => word.value.slice(p.value - 1, p.value))
const w = computed(() => word.value.slice(p.value))

//---------- Navigation ---------- //
function goToHome() {
   if (currentStep.value !== Step.LANGUAGE) {
    const confirmLeave = confirm(
      "Möchtest du das aktuelle Spiel wirklich verlassen?"
    )
    if (!confirmLeave) return
  }
  // kompletter Spiel-Reset
  selectedLanguage.value = null
  p.value = null
  word.value = ""
  i.value = 1
  history.value = []
  currentStep.value = Step.LANGUAGE
  validationResult.value = null

  // Navigation zur Startseite
  router.push("/")
}

function startGame(langId) {
  history.value = []
  selectedLanguage.value = langId
  demonChoosesP()
  word.value = ""
  currentStep.value = Step.WORD_SELECT
}
// Nächster Schritt
function goNext(step) {
  history.value.push(currentStep.value)
  currentStep.value = step
}
// Vorheriger Schritt
function goBack() {
  if (history.value.length > 0) {
    currentStep.value = history.value.pop()
  } else {
    selectedLanguage.value = null
    p.value = null
    word.value = ""
    currentStep.value = Step.LANGUAGE
  }
}
// Neustart mit gleicher Sprache
function restartSameLanguage() {
  demonChoosesP()
  word.value = ""
  i.value = 1
  validationResult.value = null
  history.value = []
  currentStep.value = Step.WORD_SELECT
}
// Zum Pumpen wechseln
function startPumping() {
  i.value = 1
  validationResult.value = null
  history.value.push(currentStep.value)
  currentStep.value = Step.PUMP
}

//---------- Gepumptes Wort ---------- //
const pumpedWord = computed(() => {
  return u.value + v.value.repeat(i.value) + w.value
})
// Gepumpte Segmente für farbliche Hervorhebung
const pumpedSegments = computed(() => {
  return [
    { text: u.value, class: "font-bold text-blue-600" },
    ...Array.from({ length: i.value }, () => ({
      text: v.value,
      class: "font-bold text-red-600 underline"
    })),
    { text: w.value, class: "font-bold text-green-600" }
  ]
})

// ---------- Validierung ---------- //
const validationResult = ref(null)
/*
 null  -> noch nicht geprüft
 true  -> Wort ∈ L
 false -> Wort ∉ L
*/
// Wort validieren
function validateWord() {
  const language = languageDefinitions[selectedLanguage.value]
  validationResult.value = language.isInLanguage(pumpedWord.value)
}
watch(i, () => {
  validationResult.value = null
})
</script>

<template>
  <div class="max-w-xl mx-auto space-y-8">
    <div class="flex justify-end bg-gray-50">
      <button
        class="px-4 py-2 border-2 border-red-700 text-red-700 font-bold rounded"
        @click="goToHome"
      >
        Zur Startseite
      </button>
    </div>
    <h2 class="text-2xl mt-16 font-bold text-center">Pumping Lemma Spiel </h2>

    <!-- Sprachauswahl -->
    <LanguageSelector v-if="currentStep === Step.LANGUAGE" @start="startGame" />

    <!-- Sprachdefinition -->
    <div v-if="currentStep !== Step.LANGUAGE" class="border rounded p-4 mt-1 bg-gray-50 font-mono text-m font-bold">
      <p>
        {{ languageDefinitions[selectedLanguage].description }}
      </p>
      <p v-if="currentStep === Step.PUMP">
        Wort : {{ word }}
        <br />
        Pumping-Länge: p = {{ p }}
        <br />
        Zerlegung: z = <span class="text-blue-600 font-bold">u</span>
        <span class="text-red-600 font-bold">v</span>
        <span class="text-green-600 font-bold">w</span> mit

        <span class="text-blue-600 font-bold">{{ u }}</span>
        <span class="text-red-600 font-bold">{{ v }}</span>
        <span class="text-green-600 font-bold">{{ w }}</span>

      </p>
    </div>

    <!-- Wortwahl -->
    <div v-if="currentStep === Step.WORD_SELECT">
      <p class="text-lg">
        <img src="@/assets/1F608_color.png" alt="Dämon" class="w-8 h-8 inline"> Dämon wählt
        <span class="font-mono font-bold">p = {{ p }}</span>
      </p>
      <WordSelector :language="languageDefinitions[selectedLanguage]" :p="p" v-model:word="word"
        @next="goNext(Step.DECOMPOSE)" />
    </div>

    <!-- Zerlegung -->
    <div v-if="currentStep === Step.DECOMPOSE" class="space-y-6">
      <DecompositionView :u="u" :v="v" :w="w" :p="p" :showConditions="true" />
      <button class="px-4 py-2 bg-red-700 w-full text-white rounded" @click="startPumping">
        Weiter zum Pumpen
      </button>
    </div>

    <!-- Pumpen -->
    <div v-if="currentStep === Step.PUMP" class="space-y-6">
      <!-- Zerlegung ohne Bedingungen -->
      <!-- <DecompositionView :u="u" :v="v" :w="w" :p="p" :showConditions="false" /> -->

      <PumpFactorSelector v-model:i="i" />
      <div class="border rounded p-4 bg-gray-50 space-y-2">
        <p class="font-semibold">
          Gepumptes Wort:
          <span class="font-bold text-lg font-mono">
            <span class="text-blue-600">u</span>
            <span class="text-red-600">v</span>
            <sup class="text-red-600">{{ i }}</sup>
            <span class="text-green-600">w</span>
          </span>
        </p>
        <p class="font-mono break-all text-lg">
          <span v-for="(segment, index) in pumpedSegments" :key="index" :class="segment.class">
            {{ segment.text }}
          </span>
        </p>
      </div>

      <!-- Validierung -->
      <button class="px-4 py-2 bg-red-700 w-full text-white rounded" @click="validateWord">
        Wort überprüfen
      </button>

      <!-- Ergebnis -->
      <div v-if="validationResult !== null" class="p-4 rounded text-lg pointer-events-none" :class="validationResult
        ? 'bg-red-100 text-red-800'
        : 'bg-green-100 text-green-800'">
        <p v-if="validationResult">
          ❌ Das Wort ist <strong>immer noch</strong> in der Sprache.<br />
          Du hast verloren.
        </p>
        <p v-else>
          ✅ Das Wort ist <strong>nicht mehr</strong> in der Sprache
          (<span class="font-mono">w ∉ L</span>).<br />
          <strong>Du hast gewonnen!</strong>
        </p>
      </div>
    </div>

    <!-- Navigation -->
    <div v-if="currentStep !== Step.LANGUAGE" class="flex justify-between pt-2">
      <button class="text-sm hover:underline px-4 py-2 border-2 border-red-700 w-1/4 text-red-700 font-bold rounded"
        @click="goBack">
        Zurück
      </button>
      <button class="text-sm hover:underline px-4 py-2 border-2 border-red-700 w-1/4 text-red-700 font-bold rounded"
        @click="restartSameLanguage">
        Neustart
      </button>
    </div>
  </div>
</template>