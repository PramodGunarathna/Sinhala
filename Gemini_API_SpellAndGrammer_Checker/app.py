from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import re

app = Flask(__name__)

# Configure the Gemini API
genai.configure(api_key="AIzaSyD_D6N3kEJydTcYpnppprt711kTN49XaAo")

def analyze_and_correct(input_text):
    model = genai.GenerativeModel('gemini-pro')
    prompt = (
        f"Analyze this Sinhala sentence: '{input_text}'\n"
        "Respond in the following format exactly:\n"
        "Subject: [subject]\n"
        "Object: [object]\n"
        "Tense: [tense]\n"
        "Errors: [errors]\n"
        "Corrected: [corrected sentence]"
    )
    response = model.generate_content(prompt)
    return response.text

def extract_subject_from_response(response_text):
    match = re.search(r'Subject:\s*(.+?)(?:\n|$)', response_text)
    return match.group(1) if match else "Subject not found"

def extract_object_from_response(response_text):
    match = re.search(r'Object:\s*(.+?)(?:\n|$)', response_text)
    return match.group(1) if match else "Object not found"

def extract_tense_from_response(response_text):
    match = re.search(r'Tense:\s*(.+?)(?:\n|$)', response_text)
    return match.group(1) if match else "Tense not found"

def extract_corrected_sentence(response_text):
    match = re.search(r'Corrected:\s*(.+?)(?:\n|$)', response_text)
    return match.group(1) if match else "Corrected sentence not found"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_subject', methods=['POST'])
def analyze_subject():
    data = request.json
    input_text = data.get("text", "")
    if not input_text:
        return jsonify({"error": "No text provided"}), 400
    
    response_text = analyze_and_correct(input_text)
    subject = extract_subject_from_response(response_text)
    
    return jsonify({"subject": subject})

@app.route('/analyze_object', methods=['POST'])
def analyze_object():
    data = request.json
    input_text = data.get("text", "")
    if not input_text:
        return jsonify({"error": "No text provided"}), 400
    
    response_text = analyze_and_correct(input_text)
    obj = extract_object_from_response(response_text)
    
    return jsonify({"object": obj})

@app.route('/analyze_tense', methods=['POST'])
def analyze_tense():
    data = request.json
    input_text = data.get("text", "")
    if not input_text:
        return jsonify({"error": "No text provided"}), 400
    
    response_text = analyze_and_correct(input_text)
    tense = extract_tense_from_response(response_text)
    
    return jsonify({"tense": tense})

@app.route('/correct_sentence', methods=['POST'])
def correct_sentence():
    data = request.json
    input_text = data.get("text", "")
    if not input_text:
        return jsonify({"error": "No text provided"}), 400
    
    response_text = analyze_and_correct(input_text)
    corrected_sentence = extract_corrected_sentence(response_text)
    
    return jsonify({"corrected_sentence": corrected_sentence})

if __name__ == '__main__':
    app.run(debug=True)