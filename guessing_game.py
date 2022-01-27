import random

play = True                                                     #starts game in a loop
while play:
    print (f'\nReady to play Who Wants to Be a Millionaire? \nWell, too bad. We got this guessing game instead. \nIf you miss 7 times, the game is over.')
    game_dict = {
        'Guitars' : {'fender', 'gibson', 'epiphone', 'ibanez', 'jackson', 'martin'}, 
        'Vegetables' : {'celery', 'spinach', 'kale', 'zucchini', 'artichoke', 'cauliflower'},
        'Countries' : {'argentina', 'germany', 'austria', 'greenland', 'thailand', 'mongolia'}
        }
    
    category, word = random.choice(list(game_dict.items()))     #random choice of category
    current_word = random.choice(list(word))                    #random choice of word

    def make_underscore_list(y):                                #creates the hidden word in list form
        return ['_' for char in y]

    def make_current_list(g):                                   #creates chosen word in list form
        list_version = list(g)
        return list_version
    current_word_list = make_current_list(current_word)         #assigns chosen word list to variable

    hidden_word_list = make_underscore_list(current_word)       #assigns 'hidden' list to variable

    def compare(x, y):                                          #determines if user input is correct
        if x in y:
            return 'yes'
        else:
            return 'no'

    def replace(a_letter):                                      #replaces underscore in hidden list with correct letter
        for idx, letter in enumerate(current_word):
            if letter == a_letter:
                hidden_word_list[idx] = current_word[idx]

    tries = 0                                                     
    while tries <8 and hidden_word_list != current_word_list:   #continues loop unless attempts run out or word is completed accurately
        tries_left = 7 - tries                                  #tracks remaining attempts
        print (f'Attempts remaining: {tries_left}')
        hidden_word = ' '.join(hidden_word_list)                #assigns hidden value back to string form and adds space for visual effect
        print (f'The category is: {category.title()}.')
        print(hidden_word)
        guess = input("\nGuess a letter: ").lower()             #assigns value of user guess
        answer = compare(guess, current_word)                   #determines direction after user guess is compared to correct answer
        if answer == 'yes':
            replace(guess)
            if hidden_word_list == current_word_list:
                hidden_word = ' '.join(hidden_word_list)                       #ends game if complete word has been guessed
                print (hidden_word)
                print(f'Correct! The word was {current_word.title()}.')     
            else:
                print ("Nice job!")
        elif answer == 'no' and tries == 6:                                 #ends game if attempts are used up
            print(f'Sorry! You are out of attempts. The word was {current_word.title()}.')
            break
        else:
            print("Nope. Try again.")                           #continues loop and adds an attempt if guess is incorrect
            tries += 1
    again = input("Would you like to play again (y/n)? ").lower()      #asks user to play again                                                   
    if again == 'n':                                
        play = False                                            #sets play to False to break loop if user declines
    else:
        play = True