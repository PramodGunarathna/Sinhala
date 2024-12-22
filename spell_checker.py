# spell_checker.py
class SpellChecker:
    def __init__(self, dictionary_path):
        self.words = self.load_words(dictionary_path)

    def load_words(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            return set(word.strip() for word in file)

    def check_spelling(self, text):
        words = text.split()
        misspelled = {}
        for word in words:
            if word not in self.words:
                # Add the misspelled word and its suggestions to the dictionary
                misspelled[word] = self.suggest_corrections(word)
        return misspelled

    def correct(self, text):
        corrected_text = []
        for word in text.split():
            if word in self.words:
                corrected_text.append(word)
            else:
                corrected_word = self.suggest_correction(word)
                corrected_text.append(corrected_word)
        return " ".join(corrected_text)

    def suggest_correction(self, word):
        # Suggest a single best correction
        return min(self.words, key=lambda w: self.levenshtein_distance(word, w))

    def suggest_corrections(self, word, max_suggestions=3):
        # Suggest a list of top corrections
        # Sort by Levenshtein distance and return the closest matches
        sorted_suggestions = sorted(self.words, key=lambda w: self.levenshtein_distance(word, w))
        return sorted_suggestions[:max_suggestions]

    def levenshtein_distance(self, word1, word2):
        if len(word1) < len(word2):
            return self.levenshtein_distance(word2, word1)
        
        if len(word2) == 0:
            return len(word1)
        
        previous_row = range(len(word2) + 1)
        for i, c1 in enumerate(word1):
            current_row = [i + 1]
            for j, c2 in enumerate(word2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        
        return previous_row[-1]
