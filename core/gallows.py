from random import choice
from config import Config
from core.pictures import GALLOWS_BY_ATTEMPTS


class Gallows:
    def __init__(self):
        self.word = self._get_word()
        self.word_coding = ["_"] * len(self.word)
        self.attempts = 6
        self.unsuccess_letters = []
        self.greeting()
        self.play()

    def _get_word(self):
        words_file_path = Config.WORDS_FILE_PATH
        with open(words_file_path, "r", encoding="utf-8") as file:
            words = [word.strip() for word in file.readlines()]
        return choice(words)

    def greeting(self):
        print("Отлично, давай поиграем в Виселицу!")
        print(f"Я загадал слово, оно состоит из {len(self.word)} букв")
        print("Отгадай его")
        print("Слово:", "_" * len(self.word))

    def play(self):
        letter = input("Угадай букву которая есть в слове:")
        if letter.lower().strip() and letter.lower() in self.word:
            self.succcess(letter)
        else:
            self.unsuccess(letter)

    def succcess(self, letter):
        print("Ты угадал!")
        for i, char in enumerate(self.word, start=0):
            if char == letter.lower():
                self.word_coding[i] = char
        print("".join(self.word_coding))
        if self.word_coding.count("_") == 0:
            self.congratulate()
            return
        self.play()

    def unsuccess(self, letter):
        self.unsuccess_letters.append(letter.lower())
        print("Ты ошибся!")
        print(f"неправильные буквы: {", ".join(self.unsuccess_letters)}")
        print("".join(self.word_coding))
        self.attempts -= 1
        try:
            self.draw_gallows()
            self.play()
        except KeyError:
            print("К сожалению ты проиграл!")
            print(f"Я загадал слово: {self.word}")
            print("Игра закончена!")


    def draw_gallows(self):
        print(GALLOWS_BY_ATTEMPTS[self.attempts])

    def congratulate(self):
        print("Поздравляю! Вы выиграли!")
