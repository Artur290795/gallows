from core.gallows import Gallows
def main():
    print("Привет! Ты хочешь начать новую игру?(Введи yes если хочешь)")
    ask = input()
    
    if ask.lower()== 'yes':
        app = Gallows()
        


if __name__ == "__main__":
    main()
