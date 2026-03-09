"""
Модуль с классом Gallows - основным классом приложения
"""

import unicodedata
from random import choice
from config import Config
from pictures import GALLOWS_BY_ATTEMPTS


class Gallows:
    """Основной класс игры "Виселица"

    Управляет игровым процессом: загадывает слово, принимает буквы,
    отслеживает прогресс и отображает состояние игры.

    Attributes:
        word (str): Загаданное слово
        word_state (list[str]): Текущее состояние отгаданного слова (буквы и "_")
        attempts (int): Оставшееся количество попыток
        incorrect_letters (list[str]): Список неверно угаданных букв
    """

    def __init__(self):
        self.word = self._get_word()
        self.word_state = ["_"] * len(self.word)
        self.attempts = Config.MAX_ATTEMPTS
        self.incorrect_letters = []
        self._greeting()
        self.play()

    def _greeting(self) -> None:
        print("-----------------------------", end="\n\n")
        print("Отлично, давай поиграем в Виселицу!", end="\n\n")
        print(
            "Суть игры состоит в том, что я загадываю слово, \n"
            "и говорю сколько в нем букв, \n"
            "ты вводишь одну букву и я сообщаю тебе \n"
            "есть ли эта буква в слове, \n"
            "если есть то все отлично, если нет, я рисую виселицу, \n"
            "всего у тебя будет 7 попыток, это будет видно по состоянию виселицы",
            end="\n\n",
        )
        print(f"Я загадал слово, оно состоит из {len(self.word)} букв", end="\n\n")
        print("Отгадай его", end="\n\n")
        print("Слово:", "_" * len(self.word), end="\n\n")
        print("-----------------------------")

    def play(self) -> None:
        while self.word_state.count("_") > 0 and self.attempts >= 0:
            self._print_info()
            letter = input("Угадай букву которая есть в слове:")
            if self._is_valid_letter(letter):
                if self._was_letter_used(letter):
                    print(f'Ты уже вводил "{letter}" и он оказался не правильным, соберись!')
                else:
                    if letter.lower().strip() and letter.lower() in self.word:
                        self.process_correct_letter(letter)
                    else:
                        self.process_incorrect_letter(letter)
            else:
                print("Ты ввел не валидный символ(ы), попробуй еще раз!", end="\n\n")

    def process_correct_letter(self, letter: str) -> None:
        print("Ты угадал!", end="\n\n")
        for i, char in enumerate(self.word, start=0):
            if char == letter.lower():
                self.word_state[i] = char

        if self.word_state.count("_") == 0:
            self._congratulate()
            return

    def process_incorrect_letter(self, letter: str) -> None:
        self.incorrect_letters.append(letter.lower())
        self.attempts -= 1
        try:
            self._draw_gallows()
        except KeyError:
            print("К сожалению ты проиграл!")
            print(f"Я загадал слово: {self.word}")
            print("Игра закончена!")

    def _draw_gallows(self) -> None:
        print(GALLOWS_BY_ATTEMPTS[self.attempts], end="\n\n")

    def _congratulate(self) -> None:
        print("Поздравляю! Ты выиграл!", end="\n\n")

    def _is_valid_letter(self, value: str) -> bool:
        return len(value) == 1 and "CYRILLIC" in unicodedata.name(value)

    def _was_letter_used(self, letter: str) -> bool:
        return letter.lower() in self.incorrect_letters

    def _get_word(self) -> str:
        words_file_path = Config.WORDS_FILE_PATH
        with open(words_file_path, "r", encoding="utf-8") as file:
            words = [word.strip() for word in file.readlines()]
        return choice(words)

    def _print_info(self) -> None:
        if self.incorrect_letters:
            print(
                f"Неправильные буквы: {', '.join(self.incorrect_letters)}", end="\n\n"
            )
        print(f"Осталось попыток: {self.attempts + 1}", end="\n\n")
        print("".join(self.word_state), end="\n\n")
