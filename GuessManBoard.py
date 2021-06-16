def get_new_word():
    """Returns a random word from our wordlist.txt to guess """
    # with opens external files and saves it into the myfile variable (File type) and close it at the end.
    with open('wordlist.txt', "r") as myfile:
        # read each new line of the text file as a word and saves it to our list, wordlist
        wordlist = myfile.readlines()
        # removes trailing \n (new line) character from the text file for each word in our wordlist
        wordlist = [a.rstrip() for a in wordlist]
        # todo : grab a random word (Hint use random library)
        return ...


if __name__ == '__main__':
    import re
    # our maxiumum number of guesses
    max_tries = 3
    # todo: use a boolean to track if word was guessed
    guessed = ...
    # todo: keep track of all picked letters
    letters_already_picked = ...
    # todo: keep track of correctly guessed letters
    correct_letters = ...
    our_word = get_new_word()
    currently_guessed = ''
    # run gun till we have guesssed our word or ran out of tries
    while not guessed and max_tries > 0:
        if currently_guessed == '':
            # new game so let's generate our guessing string (remove the letters) and replace with underscores
            currently_guessed = re.sub(r'[a-zA-Z]', r'_ ', our_word)
            print("Welcome to our guessing game! This is our word")
        print(currently_guessed)
        letter_guessed = input("Guess a letter!")
        # todo: check to see if letter has already been picked , keep prompting till we have an unseened letter
        while ...:
            letter_guessed = input(f"Guess another letter, we have picked {letters_already_picked}!")
        if letter_guessed in our_word:
            # todo add this letter to our list of correct letters
            # fills in newly guessed letter into our current guess
            currently_guessed = ''.join([a if a in correct_letters else a + ' ' if a == " " else '_ ' for a in our_word])
            # remove any extra white spaces
            currently_guessed.rstrip()
            # todo : add this letter to our list of all letters picked
            if '_' not in currently_guessed:
                # todo: update our guess parameter
                guessed = ...
            else:
                print("Great Guess! Here's your new hint")
        else:
            # todo: Decrease guessing chance every time player guesses wrong
            print(f"Ooh Wrong guess, you have {max_tries} guesses left ")
            # todo : add this letter to our list of all letters picked

    if not guessed:
        print(f"The word was {our_word} and you had guessed {currently_guessed}")
        print("Better luck next time!")
    else:
        print("YAY!! you win!")
    # todo: if extra time add code to keep guessing words

