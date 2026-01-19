<script setup>
import { useRouter } from "vue-router"
import InfoTooltip from "@/components/InfoTooltip.vue";

const router = useRouter()

function goToLanguageSelection() {
  router.push("/languages")
}
</script>

<template>
  <div class="max-w-3xl mx-auto mt-16 space-y-12 px-6">

    <!-- Titel -->
    <section class="text-center space-y-4">
      <h1 class="text-4xl font-bold">
        Einfach pumpen?
        <span class="block text-2xl font-normal text-gray-600 mt-2">
          Das Pumping-Lemma anschaulich erklärt
        </span>
      </h1>

      <p class="text-gray-600 text-lg">
        Diese Anwendung visualisiert das Pumping-Lemma interaktiv, um dessen abstrakte
        Logik mithilfe spielerischer Exploration verständlicher darzustellen.

      </p>
    </section>
    <!-- Pumping-Lemma Erklärung -->
    <section class="space-y-4">
      <h2 class="text-2xl font-semibold">
        🔄 <strong>Pumping-Lemma</strong><InfoTooltip id="pumpingPrinciple"/>
      </h2>
      <p class="text-gray-700">
        Das Pumping-Lemma ist ein Beweisinstrument der formalen Sprachentheorie, das
        verwendet wird, um zu zeigen, dass eine Sprache nicht regulär ist.
        Es besagt, dass für reguläre Sprachen bestimmte Teile eines Wortes beliebig oft wiederholt
        werden können, ohne die Sprache zu verlassen.
      </p>
    </section>
    <!-- Spielprinzip -->
    <section class="space-y-4">
      <h2 class="text-2xl font-semibold">
        🎮 <strong>Spielprinzip</strong> <InfoTooltip id="gamePrinciple"/>
      </h2>
      <div class="space-y-3 ">
        <p>
          Das Spiel visualisiert das Pumping-Lemma für formale Sprachen in einem
          interaktiven <span class="font-medium">Dämon-vs-Spieler</span>-Prinzip.
          Der Dämon vertritt die Annahme, dass die gewählte Sprache regulär ist.
          Spieler und Dämon handeln dabei abwechselnd.
        </p>
        <p>
          <span class="text-xl">🧑‍🎓</span> Der Spieler wählt eine formale Sprache aus, die untersucht werden soll.
        </p>
        <p>
          <span class="text-xl">👹</span> Der Dämon legt eine Pumping-Länge <span class="font-mono">p</span> fest
          und vertritt die Annahme, dass die gewählte Sprache regulär ist.
        </p>
        <p>
          <span class="text-xl">🧑‍🎓</span> Der Spieler wählt ein Wort der Sprache.
        </p>
        <p>
          <span class="text-xl">👹</span> Der Dämon zerlegt das Wort in die Teile
          <span class="font-mono">u</span>,
          <span class="font-mono">v</span> und
          <span class="font-mono">w</span>.
          Der mittlere Teil <span class="font-mono">v</span> ist der pumpbare
          Abschnitt.
        </p>
        <p>
          <span class="text-xl">🧑‍🎓</span> Der Spieler entscheidet, wie oft der mittlere Teil gepumpt wird, und
          erzeugt das gepumpte Wort.
        </p>
        <p>
          ✔️ Verlässt das gepumpte Wort die Sprache, ist die Annahme des Dämons
          widerlegt – <strong>der Spieler gewinnt</strong>.
        </p>
        <p>
          ✔️ Bleibt das gepumpte Wort in der Sprache, konnte kein Widerspruch
          gefunden werden – <strong>der Dämon gewinnt</strong>.
        </p>
      </div>
    </section>

    <!-- Hinweis -->
    <section class="border-l-4 border-red-700 pl-4 bg-red-50 py-2">
      <p class="text-sm text-gray-700">
        ⚠️ <strong>Hinweis:</strong> Bei regulären Sprachen kann der Dämon im Rahmen dieses Spiels nicht
        besiegt werden, da das Pumping-Lemma keine Nicht-Regularität nachweisen kann.
      </p>
    </section>

    <!-- Navigation -->
    <section class="text-center">
      <button class="px-8 py-3 mb-5 bg-red-700 text-white rounded text-lg hover:bg-red-800"
        @click="goToLanguageSelection">
        ➡️ Zur Sprachauswahl
      </button>
    </section>
  </div>
</template>
