import random
from words import word_list

def get_word():
    word=random.choice(word_list) #chooses a random word from the list
    return word.upper() #converts the word to uppercase and returns it


def play(word):
    word_completion = "_" *len(word) #creates spaces to fill with letters
    guessed=False
    guessed_letters = [] #Holds letters the user guesses
    guessed_words = [] #Holds words the user guesses
    tries = 6 #number of lines needed to be drawn to finish the hangman picture
    print("Let's play Hangman!")
    print(display_hangman(tries)) #displays the hangman image
    print(word_completion)
    print("\n")
    while not guessed and tries>0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha(): #isalpha finds if the letter is from the alphabet
            if guess in guessed_letters:
                print("You already guessed the letter!")
            elif guess not in word:
                print(guess, "is not in the word")
                tries-=1
                guessed_letters.append(guess)
            else:
                print("Good job", guess, " is the word")
                guessed_letters.append(guess)
                word_as_list=list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess] #The enumerate() function adds a counter as the key of the enumerate object.
                for index in indices:
                    word_as_list[index]=guess #replace each underscore wih guessed letter
                word_completion = "".join(word_as_list) #converts the list back to string
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You've already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word")
                tries -= 1
                guessed_words.append((guess))
            else:
                guessed = True
                word_completion = word

        else:
            print("Not a valid guess!")
        print(display_hangman(tries))  # displays the hangman image
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats you guessed the word! You win!")
    else:
        print("Sorry, you've run out of tries. The word was " + word + ".Maybe next time!")



def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N)").upper() == "Y":
        word=get_word()
        play(word)

if __name__ == "__main__":
    main()