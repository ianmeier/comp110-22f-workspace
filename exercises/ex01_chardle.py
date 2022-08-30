"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730486481"
word = str = input("Enter a 5-character word: ") 
if len(word) != 5:
    print(exit("Error: Word must contain 5 characters"))

letter = str = input("Enter a single character: ")
if len(letter) != 1:
    print(exit("Error: Character must be a single character."))



i: int = 0  # what letter are we on? 0 is first letter (h), 4 is fifth letter (o)
j: int = 0  # what letter are we looking for, and how many times does it show up? If word is "hello", and letter is "l", we want 2


print("Searching for " + letter + " in " + word)

if word[0] == letter:
    print (letter + " found at index 0")
    i = i+1
    j = j+1
else:
    i = i+1

if word[1] == letter:
    print (letter + " found at index 1")
    i = i+1
    j = j+1
else:
     i = i+1
    
if word[2] == letter:
    print (letter + " found at index 2")
    i = i+1
    j = j+1
else:
    i = i+1

if word[3] == letter:
    print (letter + " found at index 3")
    i = i+1
    j = j+1
else:
    i = i+1

if word[4] == letter:
    print (letter + " found at index 4")
    i = i+1
    j = j+1
else:
    i = i+1

if j == 0:
    print("No instances of " + letter + " found in " + word)
else:
    j = format(j)
   
    print (j + " instances of " + letter + " in " + word)



