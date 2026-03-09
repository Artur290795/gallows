import unicodedata
from random import choice
from config import Config
from pictures import GALLOWS_BY_ATTEMPTS


class Gallows:
    def __init__(self):
        self.word = self._get_word()
        self.word_coding = ["_"] * len(self.word)
        self.attempts = 6
        self.unsuccess_letters = []
        self._greeting()
        self.play()

    def _greeting(self):
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

    def play(self):
        self._print_info()
        letter = input("Угадай букву которая есть в слове:")
        if self._is_valid_letter(letter):
            if letter.lower().strip() and letter.lower() in self.word:
                self.succcess(letter)
            else:
                self.unsuccess(letter)
        else:
            print("Ты ввел не валидный символ(ы), попробуй еще раз!", end="\n\n")
            self.play()

    def succcess(self, letter: str):
        print("Ты угадал!", end="\n\n")
        for i, char in enumerate(self.word, start=0):
            if char == letter.lower():
                self.word_coding[i] = char

        if self.word_coding.count("_") == 0:
            self._congratulate()
            return
        self.play()

    def unsuccess(self, letter: str):
        self.unsuccess_letters.append(letter.lower())
        print("Ты ошибся!", end="\n\n")
        self.attempts -= 1
        try:
            self._draw_gallows()
            self.play()
        except KeyError:
            print("К сожалению ты проиграл!")
            print(f"Я загадал слово: {self.word}")
            print("Игра закончена!")

    def _draw_gallows(self):
        print(GALLOWS_BY_ATTEMPTS[self.attempts], end="\n\n")

    def _congratulate(self):
        print("Поздравляю! Ты выиграл!", end="\n\n")

    def _is_valid_letter(self, value: str):
        return len(value) == 1 and "CYRILLIC" in unicodedata.name(value)

    def _get_word(self):
        words_file_path = Config.WORDS_FILE_PATH
        with open(words_file_path, "r", encoding="utf-8") as file:
            words = [word.strip() for word in file.readlines()]
        return choice(words)

    def _print_info(self):
        if self.unsuccess_letters:
            print(
                f"Неправильные буквы: {', '.join(self.unsuccess_letters)}", end="\n\n"
            )
        print(f"Осталось попыток: {self.attempts + 1}", end="\n\n")
        print("".join(self.word_coding), end="\n\n")
