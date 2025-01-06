// Function to make an API call for analyzing the subject
function analyzeSubject() {
    const inputText = document.getElementById('inputText').value;
    fetch('/analyze_subject', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: inputText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('subjectResult').textContent = data.subject;
    })
    .catch(error => console.error('Error:', error));
}

// Function to make an API call for analyzing the object
function analyzeObject() {
    const inputText = document.getElementById('inputText').value;
    fetch('/analyze_object', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: inputText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('objectResult').textContent = data.object;
    })
    .catch(error => console.error('Error:', error));
}

// Function to make an API call for analyzing the tense
function analyzeTense() {
    const inputText = document.getElementById('inputText').value;
    fetch('/analyze_tense', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: inputText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('tenseResult').textContent = data.tense;
    })
    .catch(error => console.error('Error:', error));
}

// Function to make an API call for correcting the sentence
function correctSentence() {
    const inputText = document.getElementById('inputText').value;
    fetch('/correct_sentence', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: inputText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('correctedResult').textContent = data.corrected_sentence;
    })
    .catch(error => console.error('Error:', error));
}
