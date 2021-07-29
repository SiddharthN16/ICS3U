#-----------------------------------------------------------------------------
# Name:        Soccer Team Chemistry Checker (main.py)
# Purpose:     Evaluate the Chemistry Between Teammates Based on Spoken Language
#
# Author:      Siddharth Nema
# Created:     19-May-2021
# Updated:     25-May-2021
#-----------------------------------------------------------------------------
# PROGRAM INSTRUCTIONS
print(''' Welcome to Chemistry Checker, the program that checks your (9) player soccer team's chemistry!\n
The text in square brackets([]) indicates the position you are entering for.
The correct format for an entry is the player's name followed by a space and the language they speak.
Currently, the following languages are supported: English, French, Spanish, German, Portuguese, and Italian.
The languages are case sensitive, please ensure the first letter is capitalized.
You will be required to enter names & languages for the (9) player slots, which consist of (3) players in each position.
The program will calculate your teams chemistry based on if the languages of player's around are similar.
Refer to the diagram in the files menu to view the layout & evaluation specifics.
After the initial chemistry is calculated, there will be an oppurtunity to replace a certain player to improve chemistry.
Follow the prompts to ensure success, Thank You.\n
''')
#-----------------------------------------------------------------------------
# VARIABLES USED
# Name + Language Spoken for Values in "Horizontal" List
nameRow = [[],[],[]]
languageRow = [[],[],[]]

# Name + Language Spoken for Values in "Vertical" List
nameColumn = [[],[],[]]
languageColumn = [[],[],[]]

positions = ["FORWARD", "MIDDLE", "DEFENDER"] # Available Positions for Players
supported = ["English", "French", "Spanish", "German", "Portuguese", "Italian"] # Supported Languages for Players


message = "" # Message to be Printed based on Chemistry Percentage
chemScore = 0 # Tally of the team's Chemistry Score
chemTotal = 24 # Maximum Team Chemistry Possible

rowOuter = 0 # Finds the Outer Index Value in a Row
rowInner = 0 # Finds the Inner Index Value in a Row
columnOuter = 0 # Finds the Outer Index Value in a Column
columnInner = 0 # Finds the Inner Index Value in a Column

playerCount = 0 # Used to find Number of Players in a Row
#-----------------------------------------------------------------------------
# GET THE NAMES + SPOKEN LANGUGE OF ALL PLAYERS
for i in range(0,3): # Number of Rows
	while playerCount < 3: # Number of Players Per Row
		playerID = input(f"[{positions[i]}] Enter Name + Language for Player {playerCount+1}:\n") # Enter Name + Spoken Language
		playerSplit = playerID.split() # Split the Entry into (2) Parts (Name[0] & Language[1])

		if playerSplit[1] in supported: # Check if the Entered Language is Supported
			nameRow[i].append(playerSplit[0]) # Add Names of Players in same Row
			languageRow[i].append(playerSplit[1]) # Add Langauges of Players in same Row

			nameColumn[playerCount].append(nameRow[i][playerCount]) # Add Names of Players in Same Column
			languageColumn[playerCount].append(languageRow[i][playerCount]) # Add Languages of Players in Same Column
			playerCount+=1 # Cycle to to the next index in Row
		else: # Ask User to Re-Enter, if Language not Supported
			print(f"{playerSplit[0]}'s Langauge is currently not Supported. Please Pick a New Player\n")
	playerCount = 0 # Resets the Value for the next Row to add Players
#-----------------------------------------------------------------------------
# FINDING PLAYERS BEFORE AND AFTER FOCUSED PLAYER & CALCULATING CHEMISTRY
def chemCalc(): # Function Used to be Able to Reuse Later
	# Making the Variables Global for Use & Modification in Function and Throughout Program
	global chemScore
	global chemPercent
	global message
	chemScore = 0
	for i in range(len(languageRow)): # Loop According to Number of Rows
		for x in range(len(languageRow[i])): # Loop According to Number of Entries per Row

			playerBefore = [None] + languageColumn[i][:-1] # Calculate the Player Before a Certain one
			playerAfter = languageColumn[i][1:] + [None] # Calculate the Player After a Certain One

			# Use of ONLY if Statements is ON PURPOSE to Ensure all of them are Checked & Executed
			if languageColumn[i][x] == playerAfter[x]: # If Language of Player Below in Column Matches Focused One, Chemistry Increases
				chemScore += 1
			if languageColumn[i][x] == playerBefore[x]: # If Language of Player Above in Column Matches Focused One, Chemistry Increases
				chemScore += 1

			if languageRow[i][x] == playerAfter[x]: # If Language of Player After in Row Matches Focused One, Chemistry Increases
				chemScore += 1
			if languageRow[i][x] == playerBefore[x]: # If Language of Player Before in Row Matches Focused One, Chemistry Increases
				chemScore += 1
	chemPercent = int((chemScore / chemTotal) * 100) # How Chemistry is Calculated in (%)

	# Messages Based on Chemistry Percentage
	if chemPercent >= 0 and chemPercent <= 40:
		message = "Poor Communication, Could Use Some Work."
	elif chemPercent > 40 and chemPercent <= 70:
		message = "Pretty Good, Your Team will Communicate Well."
	elif chemPercent > 70 and chemPercent <= 90:
		message = "Excellent, Communication is on Point."
	else:
		message = "PERFECTION!"
chemCalc() # Run the chemCalc Function

print(f"Your Team Chemistry is {chemPercent}%. {message}")
#-----------------------------------------------------------------------------
# REPLACING PLAYERS
change = "" # Determines if a Player Change is Requested
loopState = True # Rare Case for using While True Loop
while change != "N" and change != "n": # Loop Occurs While change is not "N", Ends when Change is "Y"
	change = input("Would you like to Change a Player?(Y/N) ")

	if change == "Y" or change == "y": # Process of Changing Players Occurs when "Y" is Entered
		while loopState: # Loop Runs until loopState is False
			changePlayer = input("State the Player's Name to be Replaced: ")

			# The Two For Loops can't be combined; Both Loop a Different Amount of Times
			for i in range(0,3): # Max Number of Loops; Number of Rows
				if changePlayer in nameRow[i]: # Checks if the Player Requested to Change is in the Row List
					rowInner = nameRow[i].index(changePlayer) # Finds the Index of the Replacing Player in a Specific Row
					rowOuter = i # Finds the Row the Replacing Player is in
					loopState = False # Used to End the Loop & Move onto Next Part
					break # Break to prevent extra looping; Stops when the Replacing Player is Found

			for i in range(0,3): # Max Number of Loops; Number of Rows
				if changePlayer in nameColumn[i]: # Checks if the Player Requested to Change is in the Column List
					columnInner = nameColumn[i].index(changePlayer) # Finds the Index of the Replacing Player in a Specific Column
					columnOuter = i # Finds the Column the Replacing Player is in
					loopState = False # Used to End the Loop & Move onto Next Part
					break # Break to prevent extra looping; Stops when the Replacing Player is Found

			else: # If the Replacing Player is not in the List, it Loops Again to Retry
				print(f"{changePlayer} is not in the List, Try Again\n")

		# loopState = True # Reset loopState if while Loop is repeated

		playerReplace = input("Enter the Replacement Player + Language: ")
		replaceSplit = playerReplace.split() # Splits the Entry into Name & Language

		if replaceSplit[1] in supported: # Checks if the Language is Supported
			nameRow[rowOuter][rowInner] = replaceSplit[0] # The Replacing Player takes the Place of the Original Player
			languageRow[rowOuter][rowInner] = replaceSplit[1] # The Replacing Player's Languages takes Place of Original Player's Language
			nameColumn[columnOuter][columnInner] = replaceSplit[0] # The Replacing Player takes the Place of the Original Player
			languageColumn[columnOuter][columnInner] = replaceSplit[1] # The Replacing Player's Languages takes Place of Original Player's Language
			chemCalc() # Reruns the chemCalc Function, to Calculate Team chemistry

		elif replaceSplit[1] not in supported: # If the Replacing Player's Language is not Supported, Retry.
			print(f"{replaceSplit[0]}'s Langauge is currently not Supported. Please Pick a New Player\n")

	elif change == "N" or change == "n": # If not Wanting to Change Player, Final Team Chemistry is Printed
		print(f"Your Final Team Chemistry is {chemPercent}%. {message}")
#-----------------------------------------------------------------------------
