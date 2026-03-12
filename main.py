"""
Точка входа в приложение
"""

from gallows import Gallows
from word_repository import WordRepository
from engine import GallowEngine
from console_ui import ConsoleUI



def main():
    """Точка входа в игру "Виселица"

    Запрашивает у пользователя желание начать игру
    и запускает игровой процесс при положительном ответе.
    """
    print("Привет! Ты хочешь поиграть в Виселицу?(Введи yes если хочешь)")
    response = input()
    while response.lower() == "yes":
        repo = WordRepository()
        word = repo.get_word()
        engine = GallowEngine(word)
        app = ConsoleUI(engine)
        app.run()
        print("Ты хочешь сыграть еще раз?(Введи yes если хочешь)")
        response = input()

    print("Всего хорошего! Если захочешь поиграть, просто запусти приложение снова")


if __name__ == "__main__":
    main()
