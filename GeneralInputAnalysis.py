#from GeneralInput import inputFunction
def NumberFinder(wordList):
    numberWords=["one","first","second"]
    for word in wordList:
        for i in range(10):
            if str(i) in word:
                a=True
                for j in word:
                    if j in "0123456789":
                        continue
                    a=False
                if a==True:    
                    return int(word)
    if "one" in wordList:
          return 1
    if "first" in wordList:
        return 1
    if "second" in wordList:
        return 2
    return 1

def inputBreakdown (wordList):
    specType=["normal","fire","fighting","water","flying","grass","poison","electric","ground","psychic","rock","ice","bug","dragon","ghost","dark","steel","fairy"]
    UsslessWords=["me","i","am","a","is"]
    quest=False #out 
    types=False #info what type is a charizard
    number=False #info which number/id is a ...?
    amount=False #info how many fire pokemon are there
    best=False #info show me the top 5 pokemon     what is the best pokemon
    worst=False #info oposite of best
    isa=False #out
    speciaType=False #info finds if the user is asking for a spec type
    All=False #info finds if the user is asking for all pokemon
    specialTypeRequest=[]
    questList=["which","what","how","tell","do"]
    typeList=["type","kind"]
    bestList=["best","popular","top"]
    numberList=["number"]
    amountList=["many"]
    worstList=["worst","last"]
    for words in reversed(wordList):
        if words in specType:
            speciaType=True
            specialTypeRequest=specialTypeRequest+[words]
            word=specialTypeRequest[-1]
            wordList.remove(words)
            word=word.capitalize()
            specialTypeRequest[-1]=word
           
        if words in questList:
            wordList.remove(words)
            quest=True
        if words in typeList:
            wordList.remove(words)
            types=True
        if words in  numberList:
            wordList.remove(words)
            number=True
        if words in  amountList:
            wordList.remove(words)
            amount=True
        if words in  bestList:
            wordList.remove(words)
            best=True
        if words in  worstList:
            wordList.remove(words)
            worst=True
        if words in UsslessWords:
            wordList.remove(words)
    if "all" in wordList:
        wordList.remove("all")
        All=True
    if  ("is" in wordList) and (("a" in wordList) or ("an" in wordList)):
        wordList.remove("is")
        if "a" in wordList:   
            wordList.remove("a")
        else :
            wordList.remove("an")
        isa=True
    if ("is" in wordList) or ("are" in wordList) and ("there" in wordList):
        All=True
        wordList.remove("there")
        if "is" in wordList:
            wordList.remove("is")
        else:
            wordList.remove("are")

    reqNumber = NumberFinder(wordList)
    #print(" quest "+str(quest)+"\n",
    #"types "+str(types)+"\n","number "+str(number)+"\n",
    #"amount "+str(amount)+"\n","best "+str(best)+"\n",
    #"worst "+str(worst)+"\n","isa "+str(isa)+"\n",
    #"genre "+str(genre)+"\n",str(reqNumber)+" "+str(speciaType))
    OutputInfo=[quest,isa,wordList]
    InfoListPokemon=[types,amount,best,worst,speciaType,specialTypeRequest,reqNumber,wordList,All,number]
    returnList=[InfoListPokemon,OutputInfo]
    return returnList

#wordList=inputFunction()
#words=wordList[0]
#print(inputBreakdown(words))
#words=inputBreakdown(words)
#print(words[-2])
#NoneType