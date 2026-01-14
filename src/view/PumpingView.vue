<script setup>
import { ref, computed, watch } from "vue"
import { languageDefinitions } from "@/logic/languageDefinitions"
import { computeP, getDecompositions, pumpWord } from "@/logic/pumpingUtils"
import { useRouter } from "vue-router"


//---------- Komponenten ---------- //
import LanguageSelector from "@/components/LanguageSelector.vue"
import WordSelector from "@/components/WordSelector.vue"
import DecompositionView from "@/components/DecompositionView.vue"
import PumpFactorSelector from "@/components/PumpFactorSelector.vue"
import InfoTooltip from "@/components/InfoTooltip.vue"


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
// ---------- Dämon wählt Index  ---------- //
const demonIndex = ref(0)
//---------- alle möglichen Zerlegungen ---------- //
const decompositions = computed(() => {
  if (!selectedLanguage.value) return []
  if (!word.value) return []
  if (word.value.length < p.value) return []

  return getDecompositions(languageDefinitions[selectedLanguage.value], word.value, p.value)
})
//---------- Zerlegung uvw ---------- //
const decomposition = computed(() =>
  decompositions.value[demonIndex.value]
)

// ---------- bei Änderung: neue zufällige Dämon-Zerlegung ---------- //
watch(decompositions, (list) => {
  if (list.length > 0) {
    demonIndex.value = Math.floor(Math.random() * list.length)
  }
})

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
  console.log(word.value.slice(p.value));

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
const pumped = computed(() => {
  if (!decomposition.value) return ""
  return pumpWord(decomposition.value, i.value)
})
// Gepumpte Segmente für farbliche Hervorhebung
const pumpedSegments = computed(() => {
  return [
    { text: decomposition.value?.u, class: "part-u" },
    ...Array.from({ length: i.value }, () => ({
      text: decomposition.value?.v,
      class: "part-v"
    })),
    { text: decomposition.value?.w, class: "part-w" }
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
  validationResult.value = language.isInLanguage(pumped.value)
}
const examplesIn = computed(() =>
  languageDefinitions[selectedLanguage.value].examples.filter((w) => languageDefinitions[selectedLanguage.value].isInLanguage(w))
)

const examplesOut = computed(() =>
  languageDefinitions[selectedLanguage.value].examples.filter((w) => !languageDefinitions[selectedLanguage.value].isInLanguage(w))
)
watch(i, () => {
  validationResult.value = null
})
</script>

<template>
  <div class="max-w-xl mx-auto space-y-8">

    <div class="flex items-center justify-between bg-gray-50 px-6 py-4 mt-6 rounded-lg shadow-sm">
      <h2 class="text-2xl font-bold">
        Pumping Lemma Spiel
      </h2>

      <button
        class="px-4 py-2 border-2 border-red-700 text-red-700 font-bold rounded hover:bg-red-700 hover:text-white transition"
        @click="goToHome">
        Zur Startseite
      </button>
    </div>

    <!-- Sprachauswahl -->
    <LanguageSelector v-if="currentStep === Step.LANGUAGE" @start="startGame" />

    <!-- Sprachdefinition -->
    <div v-if="currentStep !== Step.LANGUAGE" class="border rounded p-4 mt-1 bg-gray-50 font-mono text-m font-bold">
      <p>
        {{ languageDefinitions[selectedLanguage].description }}
        <!-- ℹ️ Info bleibt beim Pumpen & Wortauswahl sichtbar -->
        <InfoTooltip
          id="languageInfo"
          :data="{ examplesIn, examplesOut }"
        />
      </p>
      <p v-if="currentStep === Step.PUMP">
        Wort : {{ word }}
        <br />
        Pumping-Länge: p = {{ p }}
        <br />
        Zerlegung: z = <span class="part-u">u</span>
        <span class="part-v">v</span>
        <span class="part-w">w</span> mit

        <span class="part-u">{{ decomposition.u }}</span>
        <span class="part-v">{{ decomposition.v }}</span>
        <span class="part-w">{{ decomposition.w }}</span>

      </p>
    </div>

    <!-- Wortwahl -->
    <div v-if="currentStep === Step.WORD_SELECT">
      <p class="text-lg">
        👹 Dämon wählt
        <span class="font-mono font-bold">p = {{ p }}</span>
        <InfoTooltip id="pumpingLength" />
      </p>
      <WordSelector :language="languageDefinitions[selectedLanguage]" :p="p" v-model:word="word"
        @next="goNext(Step.DECOMPOSE)" />
    </div>

    <!-- Zerlegung -->
    <div v-if="currentStep === Step.DECOMPOSE" class="space-y-6">
      <DecompositionView :u="decompositions[0].u" :v="decompositions[0].v" :w="decompositions[0].w" :p="p" />
      <button class="px-4 py-2 bg-red-700 w-full text-white rounded" @click="startPumping">
        Weiter zum Pumpen
      </button>
    </div>

    <!-- Pumpen -->
    <div v-if="currentStep === Step.PUMP" class="space-y-6">
      <PumpFactorSelector v-model:i="i" />
      <div class="border rounded p-4 bg-gray-50 space-y-2">
        <p class="font-semibold">
          Gepumptes Wort:
          <span class="font-bold text-lg font-mono">
            <span class="part-u">u</span>
            <span class="part-v">v</span>
            <sup class="part-v">{{ i }}</sup>
            <span class="part-w">w</span>
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
        ⬅️ Zurück
      </button>
      <button class="text-sm hover:underline px-4 py-2 border-2 border-red-700 w-1/4 text-red-700 font-bold rounded"
        @click="restartSameLanguage">
        🔁 Neustart
      </button>
    </div>
  </div>
</template>