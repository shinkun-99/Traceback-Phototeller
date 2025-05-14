<template>
  <div id="app" spellcheck="false">
    <h1 v-show="showTitle" class="fade-in-title">TraceBack: PhotoTeller</h1>
    <p class="welcome-text">{{ displayedText }}</p>
    <UploadPanel />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import UploadPanel from './components/UploadPanel.vue'

const fullText = '你好，我是 TraceBack。'
const displayedText = ref('')
const showTitle = ref(false)

onMounted(() => {
  // 标题显示
  showTitle.value = true

  // 欢迎语显示
  setTimeout(() => {
    let i = 0
    const typing = setInterval(() => {
      displayedText.value += fullText[i]
      i++
      if (i === fullText.length) {
        clearInterval(typing)
      }
    }, 100)
  }, 1000)
})
</script>

<style>
body {
  font-family: sans-serif;
  margin: 0;
  padding: 0;
  background-image: url('/background.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  min-height: 100vh;
  display: flex;
  align-items: center;      /* 垂直居中 */
  justify-content: center;  /* 水平居中 */
}

#app {
  text-align: center;
  max-width: 600px;
  margin: 10vh auto 5vh;
  border-radius: 10px;
}

.welcome-text {
  text-decoration: none;
  -webkit-text-decoration: none;
  font-size: 1.2rem;
  color: #333;
  min-height: 2rem;
  letter-spacing: 0.5px;
}

.fade-in-title {
  text-decoration: none;
  -webkit-text-decoration: none;
  font-size: 2rem;
  color: #222;
  opacity: 0;
  animation: fadeIn 1.5s ease-in forwards;
  animation-delay: 0.2s;
  margin-top: 1rem;
}

@keyframes fadeIn {
  to {
    opacity: 1;
  }
}
</style>


