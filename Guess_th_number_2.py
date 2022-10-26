def print_guess(number: int):
    print(f"I'm guessing the number is equal to \033[6;33;36m{number}\033[0;0m")


def user_answer() -> str:
    print("""
Have I guessed?
if so, Eter 'You Win'
if the given number is greater than yours please enter 'To big'
if the given number is less than yours please please enter 'To small'
    """)
    return input("Enter proper answer on keyboard:  ").replace(" ", "").upper()


def check_answer(choice: str) -> str:
    #print(choice)
    try:
        type(choice) == str
    except TypeError:
        print("Wrong answer, please enter answer again")
        check_answer(user_answer())
    if choice in ('YOUWIN', 'TOBIG', 'TOSMALL'):
        return choice
    else:
        check_answer(user_answer())



def game():
    """Main function of Guess the number game
    :return:
    """
    print("Guess the number between 1 and 1000 and I will guess it in max 10 tries")
    min = 0
    max = 1000
    choice = ''
    while choice != 'YOUWIN':
        if max - min > 1:

            print_guess(guess)
            choice = check_answer(user_answer())
        else:
            print("Do not cheat!")
            break
    print("I Win")


if __name__ == "__main__":
    game()
