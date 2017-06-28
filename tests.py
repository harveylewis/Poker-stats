"""
Script to read poker hands from poker stars and add statistics to table
"""

import os
import sqlite3

tourneyName = "HH20170427 T1896651582 No Limit Hold'em $0.45 + $0.05.txt"
seatsInTourney = 9




path = os.path.join(os.path.expanduser('~'), 'Desktop', 'PokerStars.UK', 'HandHistory','harveylewis6')#path to hand folder


class player(object): #Create player class

	def __init__(self, username):
		self.username = username
		self.handsDealt = 0
		self.handsContinued = 0

	def displayStats(self):
		return "Username : {}\nHands dealt = {}\nHands Continued = {}\n".format(self.username, self.handsDealt, 
			self.handsContinued)







fileName = os.path.join(path, tourneyName)
openTourney = open(fileName)
lines = openTourney.readlines()


playerList=[]

for i in range(seatsInTourney):
	for line in lines:
		if 'Seat {}'.format(i) in line:
			firstSpace = (" ".join(line.split()[2:-1]))
			endIndex = firstSpace.find(' ')
			playersUsername = firstSpace[0:endIndex]
			playerList.append(playersUsername)

usernameList = list(set(playerList))


playerObjectsList=[]

for name in usernameList:
	playerObjectsList.append(player(name))






for line in lines:
	for i in range(len(playerObjectsList)):	
		if playerObjectsList[i].username in line and 'Seat' in line:
			playerObjectsList[i].handsDealt += 1


for i in range(len(playerObjectsList)):
	print playerObjectsList[i].displayStats()










# handsDealt = 0 #initiate hands dealt
# handsWon = 0

# tournamentTypeStartIndex = filename.find('Tournament #')
# tourneyCode = str(filename[12:23])

# amountStartIndex = filename.find('$')
# amountEndIndex = (filename.find('$', int(amountStartIndex + 1))) + 5
# tourneyType = str(filename[amountStartIndex:amountEndIndex])

# gamesPlayed +=1

# newPath = os.path.join(path, filename)


# tourneyFile = open(newPath) #Opens tourney







# summaryStartLineNumbers=[]
# summaryEndLineNumbers=[]


# lines = tourneyFile.readlines()
# print lines[37]


# for num, line in enumerate(tourneyFile, 1):
#     if '*** SUMMARY ***' in line:
#         summaryStartLineNumbers.append(num + 1)

# for number in summaryStartLineNumbers:
# 	newNum = number + 13
# 	summaryEndLineNumbers.append(newNum)



