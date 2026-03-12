"""
Модуль содержит класс WordRepository, отвечающий за получение слов для игры "Виселица".
"""

from random import choice
from config import Config


class WordRepository:
    """
    Репозиторий слов для игры "Виселица".

    Загружает слова из файла и предоставляет случайное слово
    для использования в игровом процессе.
    """

    def get_word(self) -> str:
        with open(Config.WORDS_FILE_PATH, encoding="utf-8") as file:
            word = [word.strip() for word in file.readlines()]
        return choice(word)
