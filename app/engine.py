"""
Модуль с игровым движком для игры "Виселица".

Содержит основную логику игры: проверку букв, обновление состояния,
отслеживание попыток и определение победы/поражения.


"""
import unicodedata
from config import Config
from app.guess_result import GuessResult


class GallowEngine:
    """
    Игровой движок, управляющий состоянием и логикой игры "Виселица".

    Этот класс инкапсулирует всё состояние игры: загаданное слово,
    текущее состояние отгаданных букв, оставшиеся попытки,
    использованные буквы и флаги окончания игры.
    
    Attributes:
        word (str): Загаданное слово.
        word_state (list[str]): Текущее состояние угаданных букв
            (например, ['_', 'о', '_'] для слова "кот").
        attempts (int): Количество оставшихся попыток (ошибок).
        used_letters (set[str]): Множество уже введенных букв.
        is_game_over (bool): Флаг окончания игры (победа или поражение).
        is_success (bool): Флаг победы (True, если игрок выиграл).

    Methods:
        guess(letter): Основной метод для обработки хода игрока.
        incorrect_guess(): Обработка неверной догадки.
        correct_guess(letter): Обработка верной догадки.
    """
    def __init__(self, word: str):
        self.word = word
        self.word_state = ["_"] * len(self.word)
        self.attempts = Config.MAX_ATTEMPTS
        self.used_letters = set()
        self.is_game_over = False
        self.is_success = False

    def guess(self, letter: str) -> GuessResult:
        if self._was_letter_used(letter):
            return GuessResult.ALREADY_USED
        if not self._is_valid_letter(letter):
            return GuessResult.INVALID
        self.used_letters.add(letter.lower())
        if letter.lower() not in self.word:
            return self.incorrect_guess()
        return self.correct_guess(letter)

    def incorrect_guess(self) -> GuessResult:
        self.attempts -= 1
        if self.attempts > 0:
            return GuessResult.INCORRECT
        self.is_game_over = True
        return GuessResult.LOSE

    def correct_guess(self, letter: str) -> GuessResult:
        for i, char in enumerate(self.word):
            if char == letter.lower():
                self.word_state[i] = char

        if self.word_state.count("_") != 0:
            return GuessResult.CORRECT
        self.is_game_over = True
        self.is_success = True
        return GuessResult.WIN

    def _was_letter_used(self, letter: str) -> bool:
        return letter.lower() in self.used_letters

    @staticmethod
    def _is_valid_letter(value: str) -> bool:
        return len(value) == 1 and "CYRILLIC" in unicodedata.name(value)
