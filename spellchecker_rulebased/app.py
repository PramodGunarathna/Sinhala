from flask import Flask, render_template, request, jsonify
from spell_checker import SpellChecker

app = Flask(__name__)
spell_checker = SpellChecker('vertopal.com_sinhala_list.txt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_spelling():
    data = request.json
    text = data.get('text', '')
    corrected_text = spell_checker.correct(text)
    return jsonify({'corrected_text': corrected_text})

if __name__ == '__main__':
    app.run(debug=True)
