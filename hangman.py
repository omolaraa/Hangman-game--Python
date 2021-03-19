import random
print('HANGMAN GAME')
print('Guess a letter or word until the hangman drawing is complete.')
words = ['apple', 'bag', 'candy', 'dance', 'earth']
# random.choice is used to select random words
word = random.choice(words)
# The hangman drawing
symbols = ['-----', '||', '|0', '|/-+-\\', '||', '||.|', '||.|', '|', '--------']
symbols_len = len(symbols)
# Symbols to be printed will be stored here/ appended everytime the user guesses wrong
print_symbols = []
# Index for symbols
index = 0
# Letters or words that the user guesses will be stored here
guessed = []
# the number of times the user guessed right
guesses = 0
# a variable for the user input
guess = ''
# while there are still symbols available
while symbols_len > 0:
    guess = input('Guess a letter or word: \n')
    # This is to ensure that the user does not enter a blank space but  enters an alphabet
    if len(guess) > 0 and guess.isalpha():
        # if the user re-enters his/her previous guess and the guess is not part of the word, print:
        # This was done in case a guess was re-entered but is now part of the word
        if guess in guessed and guess not in word:
            print(f'You already tried {guess}, try again')
        elif guess not in word:
            print(f'{guess} is not in the word')
            # add the guess to the list of guessed words if the guess is not in the word
            guessed.append(guess)
            # add the hangman symbols to the list of print_symbols each time the user guesses wrong
            print_symbols.append(symbols[index])
            # move on to the next symbol to be appended/added
            index += 1
            # reduce the length of symbols when the user guesses wrong
            # this will keep track of how many tries/chances the user has left depending on the number
            # of symbols left
            symbols_len -= 1
            # print out all the appended/added symbols each time the user guesses wrong
            # this will increase the hangman drawing and give a complete drawing to indicate that the
            # game is over
            for each_symbol in print_symbols:
                print(each_symbol)
            print(f'You have {symbols_len} tries left')
        else:
            # the game will continue until the hangman drawing is complete
            print(f'Great job {guess} is in the word')
            guesses += 1
    else:
        # if anything other than alphabets is included, print:
        print('Invalid input!')
    # when the length of the symbols has reduced to 0, print:
    if symbols_len == 0:
        print(f'GAME OVER. \n You guessed right {guesses} times.\n The word is {word}')