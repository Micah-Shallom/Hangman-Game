import random
import time

print('\nHello and Welcome. Lets play some hangman ✨\n')

name = input('Enter Your name: ')
gender = input('Enter gender (M/F): ')

time.sleep(2)

if gender.upper() == 'M':
    print(f"Hello {name}!🧑.Best of luck")
elif gender.upper() == 'F':
    print(f"Hello {name}!👩‍🦰. Best of luck ")
else:
    print('Invalid Input. Please Retry')

time.sleep(2)
    
print('\nThe game is about to start. Lets play some hangman!!!!\n')

def mainInterface():
    global words_to_guess
    global word
    global word_display
    global word_length
    global game_count
    global already_guessed_word
    
    words_to_guess = ["february","hunger","picture","holy","descend","children","liver","baby","music","destroy","vegetation","animal", 'superstar']
    
    word  = random.choice(words_to_guess)
    word_length = len(word)
    word_display = "_"  *  word_length
    game_count = 0
    already_guessed_word = [ ]
    
    
    
def gameinterface():
    global game_count
    global word
    global word_display
    
    game_limit = 5
    
    print(word)
    
    while game_limit != game_count:
        user_guess =  input('Please guess a letter in the word :  ')
        
        #ensuring the user_guess is not an integer and it must have a length of 1.
        
        if len(user_guess.strip()) == 1 and not user_guess  <= '9' :
            
            if user_guess in word:
                already_guessed_word.extend([user_guess])
                
                found_word_index = word.find(user_guess)
                
                word_display = f"{word_display[:found_word_index]}{word[found_word_index]}{word_display[found_word_index+1 : ]}"
                
                
                word = f"{word[:found_word_index]}_{word[found_word_index + 1 : ]}"
                
                
                
                print(word)
                print(word_display)
                print(already_guessed_word)
            else:
                print('Incorrect Letter😣. Please try another letter!👍')
                game_count += 1
            
        elif len(user_guess.strip()) != 1:
            print('\n Please enter only a single letter \n')
            gameinterface()
        elif user_guess <= '9':
            print('\n Please input must be a string!!\n')
            gameinterface()
    else:
        print('Game over')
        playloop()
    
   
            
        
    
    


def playloop():
    play_choice  = input('Do you want to play game again? y=yes or n=no : ')
    
    if play_choice not in ['y' , 'Y' , 'n' , 'N']:
        print('Please Enter a valid command!!')
        playloop()
    elif play_choice in ['y' , 'Y'] :
        print('Iniitializing game...')
        time.sleep(1)
        print('Iniitializing game.........')
        time.sleep(1)
        print('Iniitializing game.............')
        time.sleep(1)
        mainInterface()
        gameinterface()
    elif play_choice in ['n' , 'N'] :
        print('Thank you for playing the hangman game!!!. Try it again sometime soon.')
        print('Made by Micah Shallom ❣❣')
        exit()
        
#Initializing the main game interface to gain access to global variables.
mainInterface()

gameinterface()



