<template>
  <div class="p-6 space-y-6">

    <!-- Sprache und n -->
    <div class="space-y-3">
      <div>
        <label for="dropdown" class="block font-semibold mb-1">Wähle eine Sprache:</label>
        <select id="dropdown" v-model="selectedLanguage" class="border rounded p-1">
          <option v-for="language in languages" :key="language" :value="language">
            {{ language }}
          </option>
        </select>
      </div>

      <div>
        <label class="block font-semibold mb-1">Wähle Wert für n:</label>
        <input type="number" v-model="n" min="1" class="block border rounded p-1" />
      </div>
    </div>

    <!-- Wortanzeige + Reset -->
    <div>
      <div class="flex items-center justify-between mb-3">
        <h3 class="font-semibold text-lg">Markiere y-Bereich im Wort:</h3>
        
      </div>

      <div class="flex flex-wrap gap-1 font-mono text-xl tracking-wide cursor-pointer select-none border rounded p-3 bg-gray-50">
          <span class="block"
            v-for="(char, index) in generatedWord.split('')"
            :key="index"
            @click="setMarker(index)"
            :style="{
              color: getTextColor(index),
              backgroundColor: getBackgroundColor(index),
              border: isBoundary(index) ? '2px solid black' : '1px solid #ccc',
              borderRadius: '4px',
              padding: '6px 10px',
              transition: 'all 0.15s ease'
            }"
          >
            {{ char }}
          </span>
          <button
            @click="resetMarkers"
            class="flex flex-wrap gap-2 bg-gray-100 hover:bg-gray-200 border border-gray-300 text-gray-800 font-medium ml-4  px-3 py-1 rounded transition"
          >
            🔄 Zurücksetzen
          </button>
      </div>
    </div>

    <!-- Zerlegung -->
    <div>
      <h2 class="text-lg font-semibold mb-2">Zerlegung:</h2>
      <ul class="space-y-1">
        <li><strong class="text-red-500">x:</strong> <code>{{ partX }}</code></li>
        <li><strong class="text-yellow-600">y:</strong> <code>{{ partY }}</code></li>
        <li><strong class="text-blue-500">z:</strong> <code>{{ partZ }}</code></li>
      </ul>
    </div>

    <!-- Pumping Bereich -->
    <div v-if="partY">
      <h2 class="text-lg font-semibold mb-2">Pumping Lemma Simulation:</h2>
      <div class="flex items-center gap-4 flex-wrap">
        <button
          @click="pumpDown"
          class="bg-red-200 hover:bg-red-300 text-red-800 font-semibold px-3 py-1 rounded transition"
        >
          ▼ Abpumpen
        </button>
        <button
          @click="pumpUp"
          class="bg-green-200 hover:bg-green-300 text-green-800 font-semibold px-3 py-1 rounded transition"
        >
          ▲ Aufpumpen
        </button>
        <span class="font-mono text-lg">i = {{ i }}</span>
        <button
          @click="checkRegularity"
          class="ml-auto bg-blue-200 hover:bg-blue-300 text-blue-900 font-semibold px-3 py-1 rounded transition"
        >
          🧠 Regulärität prüfen
        </button>
      </div>

      <div class="mt-3 font-mono text-xl bg-gray-50 p-3 rounded border">
        <strong>xy<sup>{{ i }}</sup>z:</strong>
        <div class="mt-1 break-all">{{ pumpedWord }}</div>
      </div>

      <!-- Ergebnisanzeige -->
      <div v-if="regularityResult" class="mt-3 p-3 rounded font-semibold" :class="resultClass">
        {{ regularityResult }}
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, watch } from "vue";

const n = ref(2);
const languages = ["a^n b^n"];
const selectedLanguage = ref(languages[0]);

// generiertes Wort
const generatedWord = computed(() => "a".repeat(n.value) + "b".repeat(n.value));

// Marker
const startIndex = ref(null);
const endIndex = ref(null);

// Pumping variable
const i = ref(1);

// Ergebnis Regularität
const regularityResult = ref("");
const resultClass = ref("");

// Klicklogik
function setMarker(index) {
  if (startIndex.value === null || (startIndex.value !== null && endIndex.value !== null)) {
    startIndex.value = index;
    endIndex.value = null;
  } else if (endIndex.value === null && index > startIndex.value) {
    endIndex.value = index;
  } else {
    [startIndex.value, endIndex.value] = [Math.min(startIndex.value, index), Math.max(startIndex.value, index)];
  }

  validateParts();
}

// Reset
function resetMarkers() {
  startIndex.value = null;
  endIndex.value = null;
  i.value = 1;
  regularityResult.value = "";
  resultClass.value = "";
}

// Farben
function getTextColor(index) {
  if (startIndex.value === null && endIndex.value === null) return "black";
  if (startIndex.value !== null && endIndex.value === null && index === startIndex.value) return "black";
  if (index < startIndex.value) return "red";
  if (index >= startIndex.value && index <= endIndex.value) return "orange";
  return "blue";
}

// Hintergrundfarben
function getBackgroundColor(index) {
  if (startIndex.value === null && endIndex.value === null) return "#f9fafb";

  // Nur erster Klick → Nur der gewählte Buchstabe gelb
  if (startIndex.value !== null && endIndex.value === null) {
    return index === startIndex.value ? "#fff7cc" : "#f9fafb";
  }

  // Beide Klicks gesetzt
  if (index < startIndex.value) return "#ffe5e5"; // x
  if (index >= startIndex.value && index <= endIndex.value) return "#fff7cc"; // y
  return "#e0f0ff"; // z
}

function isBoundary(index) {
  return index === startIndex.value || index === endIndex.value;
}

// Zerlegungen
const partX = computed(() => {
  if (startIndex.value === null) return "";
  return generatedWord.value.slice(0, startIndex.value);
});

const partY = computed(() => {
  if (startIndex.value === null || endIndex.value === null) return "";
  return generatedWord.value.slice(startIndex.value, endIndex.value + 1);
});

const partZ = computed(() => {
  if (endIndex.value === null) return "";
  return generatedWord.value.slice(endIndex.value + 1);
});

// Pumping Simulation
const pumpedWord = computed(() => {
  if (!partY.value) return "";
  return partX.value + partY.value.repeat(i.value) + partZ.value;
});

function pumpUp() {
  if (!partY.value) return;
  i.value++;
}

function pumpDown() {
  if (i.value > 0) i.value--;
}

// Regularitätsprüfung
function checkRegularity() {
  const word = pumpedWord.value;
  const countA = (word.match(/a/g) || []).length;
  const countB = (word.match(/b/g) || []).length;

  if (countA === countB) {
    regularityResult.value = `✅ Anzahl von a (${countA}) und b (${countB}) sind gleich → Wort bleibt in der Sprache aⁿbⁿ`;
    resultClass.value = "bg-green-100 text-green-800 border border-green-400";
  } else {
    regularityResult.value = `❌ Anzahl von a (${countA}) und b (${countB}) sind unterschiedlich → Wort verletzt Bedingung aⁿbⁿ (nicht regulär)`;
    resultClass.value = "bg-red-100 text-red-800 border border-red-400";
  }
}

// Validierung mit Dialog
function validateParts() {
  const len = generatedWord.value.length;
  if (startIndex.value === null || endIndex.value === null) return;

  if (startIndex.value === 0) {
    alert("❌ Fehler: Teil x darf nicht leer sein (|x| ≥ 1).");
    resetMarkers();
  } else if (endIndex.value >= len - 1) {
    alert("❌ Fehler: Teil z darf nicht leer sein (|z| ≥ 1).");
    resetMarkers();
  } else if (startIndex.value > endIndex.value) {
    alert("❌ Fehler: Ungültige Auswahl – Start muss vor Ende liegen.");
    resetMarkers();
  }
}

watch([startIndex, endIndex], validateParts);
</script>

<style scoped>
select,
input[type="number"] {
  display: block;
}
button {
  cursor: pointer;
}
</style>
