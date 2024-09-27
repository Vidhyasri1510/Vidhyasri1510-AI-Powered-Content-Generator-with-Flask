from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    data = request.json
    theme = data.get("theme")
    topic = data.get("topic")
    if not theme or not topic:
        return jsonify({'error': 'Both theme and topic are required'}), 400

    prompt = f"Write an article on the topic '{topic}' with the theme '{theme}'."
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return jsonify({'content': completion.choices[0].message['content']})

if __name__ == '__main__':
    app.run(debug=True)