from flask import Flask, request, jsonify, render_template
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)

# Cache models to avoid reloading each time
loaded_models = {}

def load_model(source_lang, target_lang):
    model_name = f'Helsinki-NLP/opus-mt-{source_lang}-{target_lang}'
    if model_name not in loaded_models:
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        loaded_models[model_name] = (tokenizer, model)
    return loaded_models[model_name]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data["text"]
    source_lang = data["source"]
    target_lang = data["target"]

    # Normalize language codes
    lang_map = {
        "zh-CN": "zh", "zh-TW": "zh",
        "he": "he", "jw": "jv", "fil": "tl"
    }
    source_lang = lang_map.get(source_lang, source_lang)
    target_lang = lang_map.get(target_lang, target_lang)

    try:
        tokenizer, model = load_model(source_lang, target_lang)
        inputs = tokenizer([text], return_tensors="pt", padding=True)
        translated = model.generate(**inputs)
        output = tokenizer.decode(translated[0], skip_special_tokens=True)
        return jsonify({"translated_text": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
