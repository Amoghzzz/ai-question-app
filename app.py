from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "AIzaSyDK5hmlbm1J_o_N0CdZnZI1pIQTZ8itaCE"

def ask_gemini(question):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

    headers = {"Content-Type": "application/json"}

    data = {
        "contents": [
            {
                "parts": [
                    {"text": question}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    try:
        return result['candidates'][0]['content']['parts'][0]['text']
    except:
        return "Error getting response from AI"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.json["question"]
    answer = ask_gemini(user_question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
