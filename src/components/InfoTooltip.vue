<template>
  <div class="relative inline-block">
    <!-- Info Icon -->
    <button
      class="ml-1 text-blue-500 hover:text-blue-700 font-bold"
      @click="toggle"
      aria-label="Info"
    >
      ℹ️
    </button>

    <!-- Tooltip Box -->
    <div
      v-if="open"
      class="absolute z-50 mt-2 w-96 rounded-lg border border-gray-300 bg-white pr-2 pl-2 pb-2 shadow-lg"
    >
      <!-- Text + Close Button -->
      <div class="flex items-start gap-2">
        <!-- Text -->
        <div class="whitespace-pre-line text-sm text-gray-800 pr-4">
          {{ tooltipText }}
        </div>

        <!-- Close Button -->
        <button
          class="text-gray-400 hover:text-gray-600 self-start"
          @click="close"
          aria-label="Close"
        >
          ✕
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue"

/* =========================
   PROPS
========================= */
const props = defineProps({
  id: {
    type: String,
    required: true,
  },
  data: {
    type: Object,
    required: false,
    default: () => ({})
  }
})

/* =========================
   STATE
========================= */
const open = ref(false)

/* =========================
   TOOLTIP-TEXTE (ZENTRAL)
========================= */
const TOOLTIP_TEXTS = {
  pumpingLength: `
Was ist die Pumping-Länge p?

Die Pumping-Länge p ist eine feste Zahl aus dem Pumping-Lemma.

Sie hängt nur von der Sprache ab, nicht vom gewählten Wort.

• Bei regulären Sprachen ist p vorgegeben
  (z. B. die Anzahl der Zustände eines endlichen Automaten).

• Bei nicht-regulären Sprachen wird p hier zufällig festgelegt,
  um den Dämon aus dem Pumping-Lemma zu simulieren.
`,

  decomposition: `
Zerlegung des Wortes w = uvw

Das Pumping-Lemma garantiert, dass jedes ausreichend lange Wort w
in drei Teile zerlegt werden kann:

w = u · v · w

Dabei gelten folgende Bedingungen:

• v darf nicht leer sein
• |u v| ≤ p
• v ist der pumpbare Teil

Wichtig:
Die Zerlegung wird vom Dämon gewählt.
Der Benutzer hat keinen Einfluss auf die Zerlegung.
`,

  languageInfo: (examplesIn, examplesOut) => `
Wörter in der Sprache:
${examplesIn.map(w => `• ${w === '' ? 'ε' : w}`).join('\n')}

Wörter nicht in der Sprache:
${examplesOut.map(w => `• ${w === '' ? 'ε' : w}`).join('\n')}
`
}

/* =========================
   ABGELEITETER TEXT
========================= */
const tooltipText = computed(() => {
  const entry = TOOLTIP_TEXTS[props.id]
  return typeof entry === 'function'
    ? entry(props.data.examplesIn ?? [], props.data.examplesOut ?? [])
    : entry ?? ''
})

/* =========================
   METHODS
========================= */
function toggle() {
  open.value = !open.value
}

function close() {
  open.value = false
}
</script>
