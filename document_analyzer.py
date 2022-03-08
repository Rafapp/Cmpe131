file = open('document.txt', encoding='utf8')
text = file.read()
file.close

def CountRepetitions(theText):
    theText = theText.split(" ")
    uniqueText = []
    solDict = {}

    for word in theText:
        if word not in uniqueText:
            uniqueText.append(word)
        solDict[word] = CountAppearances(word, theText)
    return solDict

def CountAppearances(aWord, aText):
    count = 0
    for word in aText:
        if(word == aWord):
            count += 1
    return count

solution = sorted(CountRepetitions(text).items(), key=lambda x: x[1], reverse=True)

for key in solution:
    print(key[0] + ": " + str(key[1]))