<script setup>
//---------- Props ---------- //
defineProps({
    u: String,
    v: String,
    w: String,
    p: Number,
    showConditions: {
        type: Boolean,
        default: true
    }
})
</script>

<template>
    <div class="space-y-4">
        <!-- Pumping-Länge -->
        <p class="text-lg">
            Pumping-Länge:
            <span class="font-mono font-bold">p = {{ p }}</span>
        </p>
        <!-- -- Wortanzeige -- -->
        <p class="text-lg font-medium">
            Wort : {{ u + v + w }}
        </p>
        <!-- - Zerlegungshinweis -- -->
        <p class="text-lg font-medium">
            <img src="@/assets/1F608_color.png" alt="Dämon" class="w-6 h-6 inline mr-2">
            Dämon zerlegt das Wort in z = uvw
        </p>

        <!-- Zerlegung -->
        <div class="text-xl font-mono space-y-1">
            <p>
                <span class="font-bold text-blue-600">u</span> = <span class="font-bold text-blue-600">{{ u }}</span>
            </p>
            <p>
                <span class="font-bold text-red-600">v</span> = <span class="font-bold text-red-600">{{ v }}</span>
            </p>
            <p>
                <span class="font-bold text-green-600">w</span> = <span class="font-bold text-green-600">{{ w }}</span>
            </p>
        </div>

        <!-- Bedingungen -->
        <!-- <div v-if="showConditions" class="text-m font-bold font-mono bg-gray-50 p-3 rounded space-y-1">
            <p>|v| = {{ v.length }} ≥ 1</p>
            <p>|uv| = {{ (u + v).length }} ≤ p</p>
        </div> -->
    </div>
</template>
