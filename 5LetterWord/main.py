
import random

 
def play_word() -> str: 
    word_bank = []
    filename = "FastAPI\menu.txt"
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            word_bank.append(word)

    return (random.choice(word_bank)).lower()


def play_game(player_word: str, random_word: str, current_guess: list[str],  misplaced_Word: list[str], incorrect_word: list[str]) -> bool:
    
    if player_word == random_word:
        return True
    
    for index, char in enumerate(player_word):
        if char == random_word[index]:
            current_guess[index] = char
            if char in misplaced_Word:
                misplaced_Word.remove(char)
        elif char not in current_guess and char not in misplaced_Word and char in random_word:
            misplaced_Word.append(char)
        elif char not in random_word and char not  in incorrect_word:
            incorrect_word.append(char)

    return False
                
        
    
def check(player_guess: str) -> bool:
    if len(player_guess) == 5 and player_guess.isalpha(): # Check if the length of the player_guess is 5 and the word is all alpha letters.
        return True
    return False




def player()-> True:
    
    max_turns = 5
    current_turn = 0
    random_word = play_word()
    current_guess = ['-', '-', '-', '-', '-',] # Current progress
    misplaced_Word = [] # The char is in random_word but in wrong position.
    incorrect_word = [] # The random_word doesnt contain this character.

    print(f'Welcome to the Word Guessing Game!\nYou have {max_turns} attempts to guess the word.')
    

    while current_turn <= max_turns:
        player_guess = str(input("Enter a word: ")).lower()
        word_check = check(player_guess)
        if word_check == True: 
            check_win = play_game(player_guess, random_word, current_guess, misplaced_Word, incorrect_word)
            if check_win:
                print(f'You have guessed the correct word.', 
                      'Congrats!!!')
                return True
                
            else:
                print(f'Current guess: {current_guess}, Turns: {current_turn}, Misplaced Word: {misplaced_Word}, Incorrect Words: {incorrect_word}')
                current_turn += 1
        else: 
            print("Only 5 and aplha letters.")


        
        
            
if __name__=="__main__":
    if player() != True:
        play_again = input('You have used up all your turns.\nBetter Luck Next Time.\nWould you like to play again (y/n): ')
        if play_again == 'y':
            player()
        else:
            print('Thanks for playing.')


