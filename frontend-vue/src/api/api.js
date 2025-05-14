// src/api/api.js
import axios from 'axios'

export const generateStory = async (photos, mood) => {
  const form = new FormData()
  photos.forEach(p => form.append("photos", p))
  form.append("mood", mood)

  const res = await axios.post("http://127.0.0.1:5000/generate", form)
  return res.data
}
