<script setup>
import InfoTooltip from "@/components/InfoTooltip.vue"

//---------- Props ---------- //
defineProps({
    u: String,
    v: String,
    
})
</script>

<template>
    <div class="space-y-4">
        <!-- - Zerlegungshinweis -- -->
        <p class="text-lg font-medium">
            👹 Dämon zerlegt das Wort in z = uvw <InfoTooltip id="decomposition" />
        </p>
        <!-- Zerlegung -->
        <div class="text-xl font-mono space-y-1">
            <p>
                <span class="part-u">u</span> = <span class="part-u">{{ u }}</span>
            </p>
            <p>
                <span class="part-v">v</span> = <span class="part-v">{{ v }}</span>
            </p>
            <p>
                <span class="part-w">w</span> = <span class="part-w">{{ w }}</span>
            </p>
        </div>
    </div>
</template>
