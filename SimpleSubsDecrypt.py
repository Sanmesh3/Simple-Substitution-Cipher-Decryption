import string

ciphertext = input("Please enter the ciphertext:\n").replace(' ', '').upper(
).translate(str.maketrans('', '', string.punctuation))

print(ciphertext)

# determine letter frequency of ciphertext
letterFrequency = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0,
                   "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0,
                   "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0,
                   "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
for letter in ciphertext:
    letterFrequency[letter] += 1

# create ordered list of letter frequency
orderedLetterFrequency = sorted(letterFrequency.items(), key=lambda item:
item[1], reverse=True)

print(orderedLetterFrequency)

# define ordered list of letter frequency based on English
englishLetterFrequency = ["e", "t", "a", "o", "i", "n", "s", "h", "r", "d",
                          "l", "u", "w", "m", "f", "c", "g", "y", "p", "b",
                          "k", "v", "j", "x", "q", "z"]

# display substitutions
substitute = dict()
for i in range(len(orderedLetterFrequency)):
    substitute[orderedLetterFrequency[i][0]] = englishLetterFrequency[i]

print(substitute)

# substitute alphabets based on frequency
plaintext = ciphertext
for i in range(0, 26):
    cipherLetter = orderedLetterFrequency[i][0]
    plainLetter = englishLetterFrequency[i]
    plaintext = plaintext.replace(cipherLetter, plainLetter)

print(plaintext.upper())
