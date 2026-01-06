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
    <!-- entweder slider oder num feld oder beides -->
    <input type="range" min="0" max="20" :value="i" @input="update($event.target.value)" class="w-full" />

    <input type="number" min="0" max="20" :value="i" @input="update($event.target.value)"
      class="w-full border rounded px-3 py-2" />
    <!-- Anzeige des gewählten Werts i -->
    <p class="text-lg">
      Gewählt: <span class="font-mono font-bold">i = {{ i }}</span>
    </p>
  </div>
</template>
