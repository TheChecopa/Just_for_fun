import random


alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',] #List of letters


def open_txt(): #This function read the file and select a random word from txt
    with open("./Hangman/list.txt", "r") as words_list:
        word = words_list.read()
        data = word.split()
        random_word = random.choice(data)
        #random_word = 'palabra'
    return list(random_word)


def available_letters(letter_user): #This function print a list of letters that have not been typed by the user
    for i in alf:
        if i in letter_user:
            alf.remove(i)
    print("Aviable letters: ", '|'.join(alf))

    
def search_letter(random_word, letter_user): #This function returns a boolean, when the word typed by the user is 
    for i in range(len(random_word)):        #inside the random word it returns true, otherwise it returns false
        if random_word[i] == letter_user:
            return True
    return False


def draw_lines(random_word, index_letter): #This function print the lines of the lenght of the word
    lines = ''
    for letter in random_word:
        if letter in index_letter:
            lines = lines + letter
        else:
            lines = lines + ' _ '
    print(lines)       


def guess_word(random_word): #This function has the necesary conditions to print the hangman
    attempts = 7
    index_letter = []
    lista = []
    while attempts > 0:
        print('-'*40)
        draw_lines(random_word, index_letter)
        letter_user = input('Guess a letter: ')
        for i in range(len(random_word)):
            lista.append(i)
        if search_letter(random_word, letter_user) and letter_user in alf:
            print('The letter is correct')
            available_letters(letter_user)
            index_letter.append(letter_user)
        elif letter_user not in alf:
            print('The letter has been gussed, try with other')
            available_letters(letter_user)
        elif lista == random_word:
            print('jajajajaj')
        else:
            attempts -= 1   
            print('The letter is incorrect,', attempts, 'remmmaning attempts')
            available_letters(letter_user)       
    if random_word == index_letter:
        print('You won, the letter is correct')
    else:
        print('Your attempts are over, you word was: ', ''.join(random_word))


if __name__ == "__main__":
    random_word = open_txt()
    guess_word(random_word)
    
