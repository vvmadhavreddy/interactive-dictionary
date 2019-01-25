import json
from difflib import get_close_matches as matches    # difflib is a library that provides classes and functions for comparing sequences.

data = json.load(open("data.json"))    # loads the json data from 'data.json' file into the program.

def getMatch(w):
    return matches(w, data.keys())[0]     # gets the best match for the input word 'w' from the keys in dict data.

def wordpedia(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(getMatch(w)) > 0:        # checks if there is any close match for the word 'w' returned by the 'getMatch' function.
        closeMatch = getMatch(w)
        userReply = input("That word does not exist, did you mean %s instead? Press Y or N: " %closeMatch)
        if userReply.lower() == 'y':
            return data[closeMatch]
        elif userReply.lower() == 'n':
            return "%s does not exist in the dictionary" %w
        else:
            return "Your reply is meaningless!"
    else:
        return "This word does not exist in the dictionary"
while True:                           # To keep iterating the whole program until it is broken by user input.
    word = input("What word do you want to know? : \n")
    output = wordpedia(word)

    if type(output) == list:          # Checks if the output is a list to iterate.
        for item in output:
            print(item)
    else:                             # if not a list print anyother data type as it is.
        print(output)

    cont = input("\nDo you want to check the meaining of another word? Y or N: ")
    if cont.lower() == 'n':
        print("\nThank You for using the dictionary.")
        break                         # breaks out of the main while loop and exits the program.
    else:
        continue                      # loop back to the start of the program.
