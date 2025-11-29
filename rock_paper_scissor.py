import random
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
def get_user_choice():
    while True:
        user_input = input("Bta kya lega... (rock, paper, ya scissors): ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid choice, please choose again.")
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Are! re! dono ka same aa gya...!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "Tu jeeta...!"
    else:
        return "Chee...Chee...Computer se haar gyaaa...!"
def play_game():
    print("Chal Suru Kerte hai...")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\nTune {user_choice} liya...")
    print(f"Computer ne {computer_choice} liya...")
    result = determine_winner(user_choice, computer_choice)
    print(f"\nResult: {result}")
play_game()