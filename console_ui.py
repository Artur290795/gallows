from engine import GallowEngine
from pictures import GALLOWS_STAGES


class ConsoleUI:
    def __init__(self, engine: GallowEngine):
        self.engine = engine

    def run(self):
        self._greeting()
        while not self.engine.is_game_over:
            self.print_info()
            letter = input("Введите букву: ")
            result = self.engine.guess(letter)

            print(result)
        if self.engine.is_success:
            ConsoleUI.congratulate()
        else:
            self.inform()

    def check_result(self, result: str, letter: str):
        if result == "Повторение":
            print(f'Ты уже вводил "{letter}", соберись!')
        elif result == "Не валидный символ":
            print("Ты ввел не валидный символ(ы), попробуй еще раз!", end="\n\n")
        elif result == "Неверный символ":
            print(GALLOWS_STAGES[self.engine.attempts], end="\n\n")
        elif result == "Угадал":
            print("Ты угадал!", end="\n\n")

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
        print(
            f"Я загадал слово, оно состоит из {len(self.engine.word)} букв", end="\n\n"
        )
        print("Отгадай его", end="\n\n")
        print("-----------------------------")

    @staticmethod
    def congratulate():
        print("Поздравляю! Ты выиграл!", end="\n\n")

    def inform(self):
        print("К сожалению ты проиграл!")
        print(f"Я загадал слово: {self.engine.word}")
        print("Игра закончена!")

    def print_info(self) -> None:
        if self.engine.used_letters:
            print(
                f"Использованные буквы: {', '.join(sorted(self.engine.used_letters))}", end="\n\n"
            )
        print("Загаданное слово:", "".join(self.engine.word_state), end="\n\n")
