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

      <p>
        Das Spiel setzt das Pumping-Lemma für formale Sprachen in einem Dämon-vs-Spieler-Prinzip um.
        Der Dämon vertritt die Annahme, dass die gewählte Sprache regulär ist.
        Er legt eine Pumping-Länge p fest und bestimmt die Zerlegung eines Wortes in die Teile
        u, v und w gemäß den Bedingungen des Pumping-Lemmas.

        Der Spieler wählt ein Wort mit einer Länge von mindestens p und bestimmt einen Pumpfaktor i ≥ 0.
        Ziel ist es zu überprüfen, ob das gepumpte Wort der Form u · vⁱ · w weiterhin zur Sprache gehört.


      </p>
      <div class="space-y-3 ">
        <p>
          👹 Der <strong>Dämon</strong> wählt die Pumping-Länge <em>p</em> und legt die Zerlegung
          <em>u</em>, <em>v</em> und <em>w</em> fest.
          Er verteidigt dabei die Annahme, dass die Sprache
          <span class="text-red-700 font-semibold underline">regulär</span> ist.
        </p>

        <p>
          🧑‍🎓 Der <strong>Spieler</strong> wählt ein Wort und einen Pumpfaktor.<br>
          Er versucht, durch geeignetes Pumpen einen Widerspruch zur Annahme des Dämons zu finden.
        </p>

        <p class="font-semibold">
          Verlässt das gepumpte Wort die Sprache →
          <span class="text-green-700">Spieler gewinnt ✔️</span>
        </p>
        <p class="font-semibold">
          Bleibt das gepumpte Wort die Sprache →
          <span class="text-red-700">Dämon gewinnt ✔️</span>
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
