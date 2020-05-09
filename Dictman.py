import json

data = json.load(open('data.json'))


def sel(word):
    if word in data:
        return data[word]
    else:
        print("Double check the word!")


word = input("enter word")
lists = sel(word)
num = 1
for i in lists:
    print(str(num) + ". " + i)
    num = num + 1
