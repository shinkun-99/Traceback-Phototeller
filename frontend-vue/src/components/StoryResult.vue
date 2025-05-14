
<template>
  <div class="story-box">
    <h3>AI 生成的故事：</h3>
    <p>{{ text }}</p>
  </div>
</template>

<script setup>
defineProps({
  text: String
})
</script>

<style scoped>
.story-box {
  background: #fff8dc;
  border: 1px solid #ccc;
  padding: 1rem;
  max-width: 600px;
  margin-top: 2rem;
  border-radius: 8px;
  white-space: pre-wrap;
}
</style>
