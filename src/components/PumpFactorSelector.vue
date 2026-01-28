<script setup>
//---------- Props ---------- //
const props = defineProps({
  i: {
    type: Number,
    required: true
  }
})
//---------- Emits ---------- //
const emit = defineEmits(["update:i"])

//---------- Update für Slider ---------- //
function update(value) {
  const v = Math.min(20, Math.max(0, Number(value)))
  emit("update:i", v)
}
</script>

<template>
  <div class="space-y-6">
    <p class="text-lg font-semibold">
      Wähle den Pumping-Faktor
    </p>
    <input type="range" min="0" max="20" :value="i" @input="update($event.target.value)"
      class="block w-full mt-0 mb-1 accent-red-600" />

    <div class="flex justify-between text-sm leading-none">
      <span v-for="n in [0, 5, 10, 15, 20]" :key="n">{{ n }}</span>
    </div>
    <!-- Anzeige des gewählten Werts i -->
    <p class="text-lg">
      Gewählter Pumping-Faktor: 
      <span class="font-mono font-bold"> 
        <span aria-live="polite" class="font-mono font-bold">
          {{ i }}
        </span>
      </span>
    </p>
  </div>
</template>
