from flask import Flask, request, jsonify
from flask_cors import CORS
# from story_generator import generate_life_story

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate():
    photos = request.files.getlist("photos")
    prompt = request.form.get("prompt", "")
    print(f"[DEBUG] 收到 {len(photos)} 张图片，提示词是：{prompt}")
    story = generate_life_story(photos, prompt)
    try:
        story = generate_life_story(photos, prompt)
        print("✅ 成功生成故事")
        return jsonify({"story": story})
    except Exception as e:
        print("❌ 生成失败：", e)
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
