<script setup>
import InfoTooltip from "@/components/InfoTooltip.vue"

//---------- Props ---------- //
defineProps({
    u: String,
    v: String,
    w: String

})
</script>

<template>
    <div class="space-y-4">
        <!-- - Zerlegungshinweis -- -->
        <p class="text-lg font-medium">
            <span class="text-xl" aria-hidden="true">👹</span>
            <span class="sr-only">Dämon</span>
            Dämon zerlegt das Wort in z = uvw
            <InfoTooltip id="decomposition" />
        </p>
        <!-- Zerlegung -->
        <div class="text-xl font-mono space-y-1">
            <p>
                <span aria-label="Teil u" class="part-u">u</span> = <span class="part-u">{{ u }}</span>
            </p>
            <p>
                <span aria-label="Teil v" class="part-v">v</span> = <span class="part-v">{{ v }}</span>
            </p>
            <p>
                <span aria-label="Teil w" class="part-w">w</span> = <span class="part-w">{{ w }}</span>
            </p>
        </div>
    </div>
</template>
