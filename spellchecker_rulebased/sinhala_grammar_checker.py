from difflib import get_close_matches

def load_sentences(file_path):
    """Load sentences from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        sentences = file.read().splitlines()
    return sentences

def correct_sentence(input_sentence, sentences):
    """Find the closest matching sentence from the list."""
    if input_sentence in sentences:
        return input_sentence  # Sentence is already correct
    else:
        # Use difflib to find a similar sentence if needed
        matches = get_close_matches(input_sentence, sentences, n=1, cutoff=0.8)
        return matches[0] if matches else None

# Main grammar check function
def grammar_check(input_sentence):
    sentences = load_sentences('D:\FlaskSpellChecker\FlaskSpellChecker\sentences.txt')
    correct_version = correct_sentence(input_sentence, sentences)
    
    print(f"Parsing sentence: {input_sentence}")
    print("Grammar Check Result:")
    if input_sentence in sentences:
        print("Grammar Status: correct")
    elif correct_version:
        print("Grammar Status: wrong grammar")
        print(f"Suggested Correction: {correct_version}")
    else:
        print("Grammar Status: wrong grammar")
        print("Suggested Correction: No correction found")

# Example input
input_sentence = "අපි ඔහුට ලියුමක් යවයි"
grammar_check(input_sentence)