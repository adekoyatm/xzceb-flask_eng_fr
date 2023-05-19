from machinetranslation import translator
from machinetranslation.translator import french_to_english, english_to_french
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench", methods=["GET"])
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    Translated_text_to_French = english_to_french(textToTranslate)
    return "Translated text to French " + Translated_text_to_French

@app.route("/frenchToEnglish", methods=["GET"])
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    Translated_text_to_English = english_to_french(textToTranslate)
    return "Translated text to English " + Translated_text_to_English

@app.route("/")
def renderIndexPage():
    return render_template("Index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
