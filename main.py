import sys, random, pprint

class Game(object):
	#Game constructor for my weird var translation from natural lanuage to ints
	def __init__(self):
		self.cpuChoice=0
		self.playerSelection=""
		self.integerTranslator = {1:"Rock",2:"Paper",3:"Scissors"}
		self.naturalLanguageTranslator = {"Rock":1,"Paper":2,"Scissors":3,"Menu":4}
	#CPU Player
	def cpuSelector(self):
		self.cpuChoice = random.randint(1,3)
		#return self.integerTranslator[self.cpuChoice]
		return self.cpuChoice
	#Player Selector
	def playerSelector(self):
		self.playerSelection=input("Rock, Paper or, Scissors? ").title()
		return self.naturalLanguageTranslator[self.playerSelection]
#New game Function with per call gamestate
def newGame(physicalPlayerCount):
	g = Game()
	gameState = {'player1':[],'player2':[]}
	#Handle player selection
	if(physicalPlayerCount==1):
		gameState['player1'].append(input("What is your name? "))
		gameState['player1'].append(g.playerSelector())
		gameState['player1'].append(0)
		gameState['player2'].append("Computer Player")
		gameState['player2'].append(g.cpuSelector())
		gameState['player2'].append(0)
		if(gameState['player1'][1]==4): sys.exit()
	elif(physicalPlayerCount==2):
		gameState['player1'][0] = input("What is your name? ")
		gameState['player2'][0] = input("What is your name? ")
		gameState['player1'][1] = g.playerSelector()
		gameState['player2'][1] = g.playerSelector()
		if(gameState['player1'][1]==4 or gameState['player2'][1]==4): sys.exit()
	else:
		print("Invalid State detected, closing")
		sys.exit(1)
	#Game logic state
	if(gameState['player1'][1] == gameState['player2'][1]):
		print("Tie!")
		mainMenu()
	if(gameState['player1'][1] == 2 and gameState['player2'][1]==1):
		print("{0} wins, selecting {1} over {2}".format(gameState['player2'][0],gameState['player2'][1],gameState['player1'][1]))
		gameState['player1'][2]+=1
	elif(gameState['player1'][1] == 3 and gameState['player2'][1]==2):
		print("{0} wins, selecting {1} over {2}".format(gameState['player2'][0],gameState['player2'][1],gameState['player1'][1]))
		gameState['player1'][2]+=1
	elif(gameState['player1'][1] == 3 and gameState['player2'][1]==1):
		print("{0} wins, selecting {1} over {2}".format(gameState['player2'][0],gameState['player2'][1],gameState['player1'][1]))
		gameState['player1'][2]+=1
	elif(gameState['player2'][1] == 2 and gameState['player1'][1]==1):
		print("{0} wins, selecting {1} over {2}".format(gameState['player1'][0],gameState['player1'][1],gameState['player2'][1]))
		gameState['player2'][2]+=1
	elif(gameState['player2'][1] == 3 and gameState['player1'][1]==2):
		print("{0} wins, selecting {1} over {2}".format(gameState['player1'][0],gameState['player1'][1],gameState['player2'][1]))
		gameState['player2'][2]+=1
	elif(gameState['player2'][1] == 3 and gameState['player1'][1]==1):
		print("{0} wins, selecting {1} over {2}".format(gameState['player1'][0],gameState['player1'][1],gameState['player2'][1]))
		gameState['player2'][2]+=1
	#Game logic End
	print("Scoreboard\n--------------\n|  {0}\t|  {1}\t|\n|  {2}\t|  (3)\t|\n-----------".format(gameState['player1'][0],gameState['player1'][1],gameState['player2'][0],gameState['player2'][1]))
#Main game menu
def mainMenu():
	menuChoice = 0
	menuChoice=int(input("Please enter a choice:\n1.See the Rules\n2.Play against the computer\n3.Play a two player game\n4.Quit\nChoice: "))
	while (menuChoice<1 and menuChoice>5):
		print("Invalid Choice")
		menuChoice=int(input("Please enter a choice:\n1.See the Rules\n2.Play against the computer\n3.Play a two player game\n4.Quit\nChoice: "))
	if(menuChoice==1): displayRules()
	if(menuChoice==2): newGame(1)
	if(menuChoice==3): newGame(2)
	if(menuChoice==4): sys.exit(1)
##Defer to menu
mainMenu()