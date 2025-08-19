import string # for checking punctuation

def validWords(inputString,inputLetters):
  inputString = inputString.lower() # change to lowercase because input letters are in lowercase
  splitString=inputString.split() # .split() splits on the parameter whitespace - creates list of the segments
  
  # Calls contains(word, inputLetters) for every words in splitString
  # inputLetters is contained in the lambda so it isn't iterated by the map
  x = list(map(lambda word: contains(word, inputLetters), splitString)) # using lambda to stop inputLetters from ALSO iterating
  return sum(x)# count of valid words
  
# Helper function to use with map
def contains(word,valid):
  for letters in word:
    #print(letters)
    if letters.isdigit(): # skip if the char is a digit
      continue
    if letters in string.punctuation: # skip if the char is punctuation
      continue
    if(letters not in valid):
      return False
  return True

print(validWords("hello world here","helowrd"))
print(validWords("hell0 world here","helowrd"))
print(validWords("hell0 world here!! !","helowrd"))
print(validWords("hello warld here","helowrd"))
print(validWords("hello worldhere","helowrd"))
