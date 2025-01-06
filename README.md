# Sinhala Spell and Grammar Checker

A comprehensive solution for spell checking and grammar correction in the Sinhala language, implementing multiple approaches including rule-based methods, machine learning models, and API integration.

## 🌟 Features

### Multiple Implementation Approaches
1. **Rule-Based System**
   - Custom implementation for Sinhala spell and grammar correction
   - Handcrafted rules based on Sinhala language structure
   - Direct pattern matching and correction

2. **Machine Learning Models**
   - Multiple architectures for comparison:
     - Regression Model
     - Bidirectional LSTM
   - Trained on comprehensive Sinhala dataset

3. **API Integration**
   - Implementation using Gemini API
   - Advanced language model capabilities
   - Enhanced accuracy for complex corrections

### Spell Checker
- Handles unique characteristics of Sinhala orthography
- Multiple correction suggestions with confidence scores
  

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

### BLEU Score Comparison
| Model | BLEU Score |
|-------|------------|
| Rule-Based | 0.40 |
| Regression | 0.33 |
| Uni-LSTM | 0.82 |
| Bi-LSTM | 0.89 |
| Gemini API | 0.46 |



## 📸 Example Outputs

### Rule-Based Approach - Spell Checker 
```
Input: කෘෂිකර්මික
Correction: කෘෂිකාර්මික
Confidence: 0.95
```

```
Input: පොලීසය
Correction: පොලීසිය
Confidence: 0.88
```

### Machine Learning Models - Grammer Checker
```
Input: ළමයි යනවා
Correction: ළමයි යති

Model: Regression
Confidence: 0.45

Model: Uni-LSTM
Confidence: 0.82

Model: Bi-LSTM
Confidence: 0.89
```

### Gemini API Implementation
```
Input: මම පාසල් යනවා
Correction: මම පාසල් යමි
Confidence: 0.78
Additional Context: Formal written form suggestion
```

## 🖼️ User Interface Screenshots


### Rule-Based Interface
![Rule-Based Spell Checker](/screenshots/rule_based_Spell_ui.jpg)
![Rule-Based Grammer Checker](/screenshots/rule_based_Grammer_ui.jpg)

### Machine Learning Models Interface
![LSTM Model Interface](/screenshots/ml_models_ui.jpg)

### Gemini API Interface
![Gemini Implementation - Spell](/screenshots/gemini_api_ui_Grammer.jpg)
![Gemini Implementation - Grammer](/screenshots/gemini_api_ui_Grammer2.jpg)

## 🚀 Getting Started

### Prerequisites
```bash
python >= 3.8
numpy
pandas
tensorflow >= 2.0
google-cloud-aiplatform  # For Gemini API
```

### Installation
1. Clone the repository
```bash
git clone https://github.com/PramodGunarathna/Sinhala_Spell_And_Grammer_Checker.git
cd Sinhala_Spell_And_Grammer_Checker
```

## 🌐 Web Application

The project includes a web-based interface that provides access to all implementation approaches:
- Rule-based checker
- Machine learning models
- Gemini API integration
- Comparison view of all approaches


## 👥 Authors
- Pramod Nadishka Gunarathna
- Pawani Kaveesha Somarathna

