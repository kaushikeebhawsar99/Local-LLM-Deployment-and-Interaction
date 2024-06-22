from gpt4all import GPT4All
from flask import Flask, request, jsonify

app = Flask(__name__)
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        prompt = data.get('prompt')
        response = model.generate(prompt)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(port=5000)
