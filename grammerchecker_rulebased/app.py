from flask import Flask, render_template, request
from difflib import get_close_matches

app = Flask(__name__)

def load_sentences(file_path):
    """Load sentences from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        sentences = file.read().splitlines()
    return sentences

def correct_sentence(input_sentence, sentences):
    """Find the closest matching sentence from the list."""
    if input_sentence in sentences:
        return input_sentence  
    else:
        
        matches = get_close_matches(input_sentence, sentences, n=1, cutoff=0.8)
        return matches[0] if matches else None

# Main grammar check function
def grammar_check(input_sentence):
    sentences = load_sentences('D:/FlaskSpellChecker/FlaskSpellChecker/sentences.txt')
    correct_version = correct_sentence(input_sentence, sentences)
    
    if input_sentence in sentences:
        return "correct", None
    elif correct_version:
        return "wrong grammar", correct_version
    else:
        return "wrong grammar", "No correction found"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_sentence = request.form['sentence']
        status, suggestion = grammar_check(input_sentence)
        return render_template('index.html', input_sentence=input_sentence, status=status, suggestion=suggestion)
    return render_template('index.html', input_sentence='', status='', suggestion='')

if __name__ == '__main__':
    app.run(debug=True)
