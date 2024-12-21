# pyspellchecker.py
from spell_checker import SpellChecker

spell_checker = SpellChecker('vertopal.com_sinhala_list.txt')
incorrect_text = "එළඹන මහ මැතවර්ණට පසුගිය ජනාධිපත්වනයට වඩා වැඩි අරක්ෂවක යෙදවමට පලීසය තරණය කර ඇත"
misspelled_words = spell_checker.check_spelling(incorrect_text)
corrected_text = spell_checker.correct(incorrect_text)

print("Misspelled Words with Suggestions:", misspelled_words)
print("Corrected Text:", corrected_text)

