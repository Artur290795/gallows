from gallows import Gallows


def main():
    print("Привет! Ты хочешь поиграть в Виселицу?(Введи yes если хочешь)")
    ask = input()

    if ask.lower() == "yes":
        app = Gallows()
    else:
        print("Всего хорошего! Если захочешь поиграть, просто запусти приложение снова")


if __name__ == "__main__":
    main()
