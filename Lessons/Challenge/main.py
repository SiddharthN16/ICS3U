#-----------------------------------------------------------------------------
# Name: Python Challenge (main.py)
# Purpose: String Manipulation & File Reading
#
# Author: Siddharth Nema
# Created: 21-June-2021
# Updated: 22-June-2021
#-----------------------------------------------------------------------------
# Reads the File & Closes it
file = open("wotw.txt", 'r',encoding='utf-8')
content = file.read()
file.close()
#-----------------------------------------------------------------------------
# COUNTS THE NUMBER OF PARAGRAPHS

# Splits the content wherever there is a new line
paragraph = content.split('\n')
paraCount = 0

# Loops through the whole book
for i in paragraph:
    # If the line is not empty, the paragraph count increases
    if bool(i):
        paraCount += 1

print(f"There are {paraCount} paragraphs.\n")
#-----------------------------------------------------------------------------
# COUNTS THE NUMBER OF SENTENCES

puncCount = 0

# Loops throw every character in book
for i in range(len(content)):
    # If any of the characters end with puncutation, the counter increases
    if content[i].endswith(".") or content[i].endswith("!") or content[i].endswith("?"):
        puncCount +=1

print(f"{puncCount} Sentences End with Punctuation.\n")

#-----------------------------------------------------------------------------
# COUNTS THE NUMBER OF WORDS

# Removes the trailing characters of the words, by default spaces
words = content.rstrip()
words = words.split()

# Finds the length of the list
wordCount = len(words)

print(f"There are {wordCount} Words in the Book.\n")
#-----------------------------------------------------------------------------
# WORD CHECK

# The count is off by +1 or -1 for some words

word = input("Enter the Word you Would Like to Check For: ")

occurCount = 0
caseCheck = None

#Loops Again if the Value for caseCheck is not an Acceptable Option
while caseCheck != 'Case' and caseCheck != 'case' and caseCheck != 'Word' and caseCheck != 'word' and caseCheck != 'Char' and caseCheck != 'char':

    caseCheck = input("Would you like to Match the Case, Match the Whole Word or just the Characters? (Case/Word/Char): ")

    # Mode #1
    if caseCheck == 'Case' or caseCheck == 'case':
        # Loops through all the words in book
        for i in range(len(words)):
            # Checks if the entered word is in the book
            if word in words[i]:
                # # Ensures that word is isolated (not part of another word), when counting as an instance, and the case of the word is followed when checking
                if ((words[i][0].isalpha() == False) or (words[i][0] == word[0])) and ((words[i][-1].isalpha() == False) or (words[i][-1] == word[-1])):
                    occurCount += 1

    # Mode #2
    elif caseCheck == 'Word' or caseCheck == 'word':
        # Converts the word into lowercase
        word = word.lower()

        # Loops through the whole book
        for i in range(len(words)):
            # Checks if the word is in the book
            if word in words[i] or word.capitalize() in words[i]:
                # Ensures that word is isolated (not part of another word), when counting as an instance
                if ((words[i][0].isalpha() == False) or ((words[i][0] == word[0]) or (words[i][0] == word[0].upper()))) and ((words[i][-1].isalpha() == False) or (words[i][-1] == word[-1])):
                    occurCount += 1

    # Mode #3
    elif caseCheck == 'Char' or caseCheck == 'char':
        # Converts the word into lowercase
        word = word.lower()

        # Loops through whole book
        for i in range(len(words)):
            # Only checks if the set of characters inputted, is in the book
            if word in words[i] or word.capitalize() in words[i]:
                occurCount+=1
    else:
        print("Not an Acceptable Response, Please Try Again.")

print(f"'{word}' Appears {occurCount} Times in the Book.")
#-----------------------------------------------------------------------------
