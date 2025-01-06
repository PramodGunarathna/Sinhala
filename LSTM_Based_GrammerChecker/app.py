from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import os
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# Load model and tokenizer
try:
    model = load_model('lstm_model3.h5')
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    app.logger.info("Model and tokenizer loaded successfully")
except Exception as e:
    app.logger.error(f"Error loading model or tokenizer: {str(e)}")

max_len = 100  

def predict_sentence(input_sentence):
    try:
        app.logger.info(f"Processing input: {input_sentence}")
        input_sequence = tokenizer.texts_to_sequences([input_sentence])
        input_padded = pad_sequences(input_sequence, maxlen=max_len, padding='post')
        predictions = model.predict(input_padded)
        predicted_sequence = tf.argmax(predictions[0], axis=-1).numpy()
        predicted_sentence = " ".join(
            [word for word in tokenizer.sequences_to_texts([predicted_sequence])[0].split() if word != "<OOV>"]
        )
        app.logger.info(f"Prediction result: {predicted_sentence}")
        return predicted_sentence
    except Exception as e:
        app.logger.error(f"Prediction error: {str(e)}")
        raise

@app.route('/')
def home():
    app.logger.info('Home page accessed')
    return render_template('index.html')

@app.route('/check_grammar', methods=['POST'])
def check_grammar():
    try:
        if request.method == 'POST':
            input_text = request.form['text']
            app.logger.info(f"Received text: {input_text}")
            corrected_text = predict_sentence(input_text)
            return jsonify({'corrected_text': corrected_text})
    except Exception as e:
        app.logger.error(f"Error in check_grammar: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)