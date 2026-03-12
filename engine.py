import unicodedata
from config import Config


class GallowEngine:
    def __init__(self, word: str):
        self.word = word
        self.word_state = ["_"] * len(self.word)
        self.attempts = Config.MAX_ATTEMPTS
        self.used_letters = set()
        self.is_game_over = False
        self.is_success = False

    def guess(self, letter: str):
        if self.was_letter_used(letter):
            return "Повторение"
        self.used_letters.add(letter.lower())
        if not self.is_valid_letter(letter):
            return "Не валидный символ"
        if letter.lower() not in self.word:
            self.attempts -= 1
            if self.attempts > 0:
                return "Неверный символ"
            self.is_game_over = True

        for i, char in enumerate(self.word):
            if char == letter.lower():
                self.word_state[i] = char

        if self.word_state.count("_") != 0:
            return "Угадал"
        self.is_game_over = True
        self.result = True


    @staticmethod
    def is_valid_letter(value: str) -> bool:
        return len(value) == 1 and "CYRILLIC" in unicodedata.name(value)

    def was_letter_used(self, letter: str) -> bool:
        return letter.lower() in self.used_letters

