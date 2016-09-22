__author__ = 'Thomas Hauth, Martin Heck'

class HangManEngine:
  def __init__(self, secretWord):
    pass

  def getMessage(self):
    return\
    'This is a game of hangman. For an explanation, please search the web.'

  def readInput(self, choosenInput=None):
    if choosenInput:
        userInput = raw_input("Please insert your letter:")
    return print("You choose an", userInput)
    '''You chose an "A" '''
    else:
	self.userInput = choosenInput
    return self.userInput
