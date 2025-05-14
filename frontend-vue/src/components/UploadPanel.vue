
<template>
  <div class="upload-panel">
    <h2>上传你的照片和心情</h2>
    <input type="file" multiple @change="handleFiles" />
    <textarea v-model="mood" placeholder="那段时间的心情是..."></textarea>
    <button @click="submit">生成故事</button>

    <StoryResult v-if="story" :text="story" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import StoryResult from './StoryResult.vue'

const mood = ref('')
const photos = ref([])
const story = ref('')

const handleFiles = (e) => {
  photos.value = Array.from(e.target.files)
}

const submit = async () => {
  const formData = new FormData()
  photos.value.forEach(file => formData.append('photos', file))
  formData.append('mood', mood.value)

  try {
    const res = await axios.post('http://127.0.0.1:5000/generate', formData)
    story.value = res.data.story
  } catch (err) {
    console.error("提交失败:", err)
    alert("生成故事时出错，请检查后端是否运行")
  }
}
</script>

<style scoped>
.upload-panel {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  margin-top: 2rem;
}
textarea {
  width: 80%;
  height: 100px;
}
</style>
