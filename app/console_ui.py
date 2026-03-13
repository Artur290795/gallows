from app.engine import GallowEngine
from app.guess_result import GuessResult
from app.pictures import GALLOWS_STAGES
from config import Config


class ConsoleUI:
    def __init__(self, engine: GallowEngine):
        self.engine = engine

    def run(self) -> None:
        self._greeting()
        while not self.engine.is_game_over:
            self.print_info()
            letter = input("Введите букву: ")
            result = self.engine.guess(letter)
            self.check_result(result, letter)

    def check_result(self, result: GuessResult, letter: str) -> None:
        if result == GuessResult.ALREADY_USED:
            self._print_info_already_used(letter)
        elif result == GuessResult.INVALID:
            self._print_info_invalid_character()
        elif result == GuessResult.INCORRECT:
            self._print_info_incorrect_character()
        elif result == GuessResult.CORRECT:
            self._print_info_correct_character()
        elif result == GuessResult.WIN:
            ConsoleUI.congratulate()
        elif result == GuessResult.LOSE:
            self.lose_inform()

    def _print_info_already_used(self, letter: str):
        print(f"Ты уже вводил '{letter}', соберись!")

    def _print_info_invalid_character(self):
        print("Ты ввел не валидный символ(ы), попробуй еще раз!", end="\n\n")

    def _print_info_incorrect_character(self):
        print("Ошибка")
        print(GALLOWS_STAGES[self.engine.attempts], end="\n\n")

    def _print_info_correct_character(self):
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
        )
        print(
            f"всего у тебя будет {Config.MAX_ATTEMPTS} попыток, это будет видно по состоянию виселицы",
            end="\n\n",
        )
        print(
            f"Я загадал слово, оно состоит из {len(self.engine.word)} букв", end="\n\n"
        )
        print("Отгадай его", end="\n\n")
        print("-----------------------------")

    @staticmethod
    def congratulate() -> None:
        print("Поздравляю! Ты выиграл!", end="\n\n")

    def lose_inform(self) -> None:
        print(GALLOWS_STAGES[self.engine.attempts], end="\n\n")
        print("К сожалению ты проиграл!")
        print(f"Я загадал слово: {self.engine.word}")
        print("Игра закончена!")

    def print_info(self) -> None:
        if self.engine.used_letters:
            print(
                f"Использованные буквы: {', '.join(sorted(self.engine.used_letters))}",
                end="\n\n",
            )
        print("Загаданное слово:", "".join(self.engine.word_state), end="\n\n")
        print(f"Осталось {self.engine.attempts} попыток")
