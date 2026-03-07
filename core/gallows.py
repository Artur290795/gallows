from random import choice
from config import Config
from core.pictures import GALLOWS_BY_ATTEMPTS


class Gallows:
    def __init__(self):
        self.word = self._get_word()
        self.attempts = 6
        print(self.word)
        self.greeting()
        self.ask_for_word()

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

    def ask_for_word(self):
        letter = input("Угадай букву которая есть в слове:")
        if letter.lower() in self.word:
            print("Ты угадал!")
        else:
            print("Ты ошибся!")
            self.attempts -= 1
            try:
                self.draw_gallows()
                self.ask_for_word()
            except KeyError:
                print('К сожалению ты проиграл!')
                print('Игра закончена!')
                

    def draw_gallows(self):
        print(GALLOWS_BY_ATTEMPTS[self.attempts])

    @property
    def get_word(self):
        return self.word
