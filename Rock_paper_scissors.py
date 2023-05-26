import random


def play():
    print('Lets play Rock-Paper-Scissors')
    print('Select any of option')
    print('1: Rock')
    print('2: Paper')
    print('3: Scissors')
    player_choice = input('Enter your choice: (1,2,3): ')

    if player_choice not in ['1', '2', '3']:
        print('Invalid choice. Please try again!')
        play()
        return

    player_choice = int(player_choice)

    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.randint(1, 3)

    print('Computer chooses: ', choices[computer_choice - 1])

    if player_choice == computer_choice:
        print('Its a tie!')
    elif (
            (player_choice == 1 and computer_choice == 3) or
            (player_choice == 2 and computer_choice == 1) or
            (player_choice == 3 and computer_choice == 2)
    ):
        print("You win!")
    else:
        print('computer wins!')

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again == "yes":
        play()
    else:
        print("Thanks for playing!")


play()
