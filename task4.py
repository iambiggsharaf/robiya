s = "Salam Almaty. We are are from Dushanbe. Aga"

myDict = {}


def isGoodWord(word):

    numOfvowels = 0
    for i in word:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            numOfvowels += 1
    
    if numOfvowels > (len(word) - numOfvowels):
        return True
    else:
        return False

def checkEachWord(text):
    for i in text.split():
        i = i.lower()
        if isGoodWord(i) == True:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1

checkEachWord(s)
print(myDict)