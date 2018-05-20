import random
import string
import sys
import os

WORDLIST_FILENAME = "palavras.txt"

class Word:
    def __init__(self, guesses):
        self.secretLetters = []
        self.secretWord = self.loadWords()
        self.lettersGuessed = []
        self.guesses = string.ascii_lowercase

    def loadWords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        # print "Loading word list from file..."

        try:
            inFile = open(WORDLIST_FILENAME, 'r', 0)

        except IOError:
            print '**** Error loading file:', WORDLIST_FILENAME, '****'
            sys.exit(0)
        
        line = inFile.readline()
        wordlist = string.split(line)
        # print "  ", len(wordlist), "words loaded."  

        choosedWord = random.choice(wordlist) 
        uniqueLetters = len(set(choosedWord))
        while (uniqueLetters > 8):
            randomChoosedWord = random.choice(wordlist) 
        return choosedWord


    def isWordGuessed(self):
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                pass
            else:
                return False

        return True

    def getAvailableLetters(self):
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase

        return available

    def validateUserGuess(self):
        guessed=''
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                guessed += letter
            else:
                guessed += '_ '
        
        return guessed
    
    def showDifferentLetters(self):
        return len(set(self.secretWord))
         
class Messages:
    def __init__(self, guesses, w):
        self.guesses = string.ascii_lowercase
        self.w = Word(guesses)

    def hangmanIntro(self):
        os.system("clear")
        print '\n[*** Welcome to the game, Hangman! ***]\n' 
        print 'I am thinking of a word that is >>', len(self.w.secretWord), '<< letters long.'
        print 'This word has >>', self.w.showDifferentLetters() , '<< different letters.'
        print '\n****************\n'
    
def hangman():

    guesses = 8
    w = Word(guesses)
    m = Messages(guesses, w)
    
    m.hangmanIntro()

    while  w.isWordGuessed() == False and guesses >0:

        print 'You have >>', guesses, '<< guesses left.'
        available = w.getAvailableLetters()

        for letter in available:
            if letter in w.lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters:', available
        letter = raw_input('Please guess a letter: ')

        if letter in w.lettersGuessed:

            print '\n****************'
            print 'Oops! You have already guessed that letter: ', w.validateUserGuess()
        
        elif letter not in string.ascii_letters:
            print '\n****************'
            print('You should try a valid letter!')

        elif letter in w.secretWord:
            w.lettersGuessed.append(letter)

            print '\n****************'
            print 'Good Guess: ', w.validateUserGuess()

        else:
            guesses -=1
            w.lettersGuessed.append(letter)

            print '\n****************'
            print 'Oops! That letter is not in my word: ',  w.validateUserGuess()
       
        print '****************\n'

    else:
        if w.isWordGuessed() == True:
            print '\n\n****Congratulations, you won!!!****\n\n'
        else:
            print 'Sorry, you ran out of guesses. The word was ', w.secretWord, '.'




hangman()
