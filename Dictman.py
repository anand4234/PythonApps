import json
import difflib
from difflib import get_close_matches

data = json.load(open('data.json'))


def sel(word):
    if word in data:
        return data[word]
    else:
        nw = get_close_matches(word, data.keys(), n=1)
        print('Did you mean ' + nw[0] + '? y or n?')
        ri = input()
        if ri == 'y':
            return data[nw[0]]
        elif ri == 'n':
            print("Try Again!")
        else:
            print("Not in dictionary!")


word = input("Enter Word?\n")
lists = sel(word.lower())
num = 1
if (lists):
    for i in lists:
        print(str(num) + ". " + i)
        num = num + 1
