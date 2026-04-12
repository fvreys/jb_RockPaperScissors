from random import choice


def user_details() -> int:
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")
    score: int = 0

    ratings = open('rating.txt', 'r')
    for rating in ratings:
        values = rating.split()
        if user_name == values[0]:
            score = int(values[1])
            break
    ratings.close()
    return score


def read_options() -> list:
    options_by_user = input()
    print("Okay, let's start")
    if options_by_user == "":
        return ['rock', 'paper', 'scissors']
    else:
        return options_by_user.split(",")


def calculate_losing_options(user_option, option_list) -> list:
    # Make a list of losing options from 'option_list' based on the user_option of the user
    user_option_index: int = option_list.index(user_option)  # Always exact one occurrence
    length_options = len(option_list)
    half_options: int = len(option_list) // 2

    # Calculate start & end of losing options in list. Use remainder to go from end to start of list
    start_losing = (user_option_index + 1) % length_options
    end_losing = (user_option_index + half_options) % length_options   # Last losing index (included) !
    if start_losing <= end_losing:
        # One slice without rotation over end of list
        losing_options = option_list[start_losing: end_losing + 1]
    else:
        # Two slices because we rotate over end of list
        losing_options = option_list[start_losing: length_options] + option_list[0: end_losing + 1]
    return losing_options


def decision(user_choice, computer_choice, score, losing_options) -> int:
    if user_choice == computer_choice:
        print(f"There is a draw ({user_choice})")
        return score + 50
    elif computer_choice not in losing_options:
        print(f"Win -> Well done. The computer chose {computer_choice} and failed")
        return score + 100
    else:
        print(f'Sorry, but the computer chose {computer_choice}')
        return score


def user_input():
    score_user: int = user_details()
    choices = read_options()
    option: str = input()

    while option != "!exit":
        if option == "!rating":
            print(f"Your rating: {score_user}")
        elif option in choices:
            computer_option = choice(choices)
            losers: list = calculate_losing_options(option, choices)
            score_user = decision(option, computer_option, score_user, losers)
        else:
            print(f"Invalid input")

        option: str = input()

    print("Bye!")


user_input()
