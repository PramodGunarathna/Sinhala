# Sinhala Spell and Grammar Checker

A comprehensive solution for spell checking and grammar correction in the Sinhala language, combining rule-based methods with machine learning approaches.

## 🌟 Features

### Spell Checker
- Custom rule-based implementation for Sinhala spell correction
- Handles unique characteristics of Sinhala orthography
- Fast and efficient correction suggestions

### Grammar Checker
- **Hybrid Approach:**
  - Rule-based system with handcrafted grammar rules
  - Machine learning models for enhanced accuracy

- **Multiple Model Architectures:**
  - Regression Model
  - Unidirectional LSTM
  - Bidirectional LSTM (Best performing)

## 📊 Dataset

The project includes a comprehensive dataset for training and evaluation:
- Annotated Sinhala text samples
- Tagged grammatical errors
- Correction pairs for model training

## 🔍 Model Evaluation

We conducted extensive evaluation of our three machine learning architectures:
- Comparative performance analysis
- Metrics: Accuracy, Precision, Recall, F1-score
- Real-world usage scenarios testing

## 🚀 Getting Started

### Prerequisites
```bash
python >= 3.8
numpy
pandas
```

### Installation
1. Clone the repository
```bash
git clone https://github.com/PramodGunarathna/Sinhala_Spell_And_Grammer_Checker.git
cd Sinhala_Spell_And_Grammer_Checker
```


## 📸 Examples

### Spell Checker Output
```
Input: කෘෂිකර්මික
Correction: කෘෂිකාර්මික
```
```
Input: පොලීසය
Correction: පොලීසිය
```
### Grammar Checker Output
```
Input: ළමයි යනවා
Correction: ළමයි යති
Confidence: 0.8837
```

## 📊 Performance

| Model | Accuracy |
|-------|----------|
| Regression | 32% |
| Bi-LSTM | 88.29% | 


## 👥 Authors

- Pramod Nadishka Gunarathna  
- Pawani Kaveesha Somarathna 

