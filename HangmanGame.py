import random

HANGMAN_PICS=['''
+-----+
       |
       |
       |
    ===''', '''
+-----+
 o    |
       |
       |
    ===''','''
+-----+
 o    |
 |     |
       |
    ===''','''
+-----+
 o    |
/|     |
       |
    ===''','''
+-----+
 o    |
/|\ |
       |
    ===''','''
+-----+
 o    |
/|\ |
/      |
    ===''','''
+-----+
 o    |
/|\ |
/ \ |
    ===''']
words='ant baboon badger bat bear cat camel clam crow deer dog donkey eagel fox frog goat skunk snake stork '.split()

def getRandomWord(wordList):
       wordIndex= random.randint(0, len(wordList)-1)
       return wordList[wordIndex]

def displayBoard(HANGMAN_PICS,missedLetters, correctLetters, secretWord):
       print(HANGMAN_PICS[len(missedLetters)])
       print()
       print('Missed Letters: ', end=' ')
       for letter in missedLetters:
              print(letter, end=' ' )
       print()

       blanks='_'* len(secretWord)
       for i in range(len(secretWord)):
              if secretWord[i] in correctLetters:
                     blanks=blanks[:i]+secretWord[i]+blanks[i+1:]
       for letter in blanks:
              print(letter, end=' ')
       print()

def getGuess(alreadyGuessed):
       while True:
              print('Guess a letter')
              guess= input()
              guess = guess.lower()
              if len(guess) !=1:
                     print('please enter a single letter')
              elif guess in alreadyGuessed:
                     print('You have already guessed that letter. Choose again')
              elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                     print('please enter a letter')
              else:
                     return guess
def playAgain():
       print('Do you wank to play again?(yes or no)')
       return input().lower().startwith('y')

print('HANGMAN')
missedLetters=''
correctLetters=''
secretWord = getRandomWord(words)
gameIsDone=False
while True:
       displayBoard(HANGMAN_PICS, missedLetters, correctLetters, secretWord)
       guess = getGuess(missedLetters+correctLetters)

       if guess in secretWord:
              correctLetters = correctLetters+guess
              foundAllLetters = True
              for i in range(len(secretWord)):
                     if secretWord[i] not in correctLetters:
                            foundAllLetters=False
                            break
              if foundAllLetters:
                            print('yes! The secretWord is"'+secretWord+'"! You have won!')
                            gameIsDone=True
       else:
              missedLetters=missedLetters+guess
              if len(missedLetters)==len(HANGMAN_PICS)-1:
                     displayBoard(HANGMAN_PICS,missedLetters, correctLetters, secretWord)
                     print('You have run out of guesses! \n After'+ str(len(missedLetters)))
                     gameIsDone=True

       if gameIsDone:
              if playAgain():
                     missedLetters=''
                     correctLetters=''
                     gameIsDone=False
                     secretWord=getRandomWord(words)
              else:
                     break
                     
