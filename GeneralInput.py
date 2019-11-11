def inputFunction (questionOriginal):                                           #used to gather information from the user
    question=questionOriginal.lower()                           # a new string that can be modified for analizing purposes
    for i in reversed(range(len(question))):
        if question[i] in "!?.":                                # deleting unneccery simbols from the input
            question=question.replace("!", '')
            questionOriginal=questionOriginal.replace("!", '')
            if len(question)==0:
                break
            question=question.replace("?", '')
            questionOriginal=questionOriginal.replace("?", '')
            if len(question)==0:
                break
            question=question.replace(".", '')
            questionOriginal=questionOriginal.replace(".", '')
            if len(question)==0:
                break
    originalWordList=questionOriginal.rsplit()                  #Spliting up the words into a list for the original input
    wordList=question.rsplit()                                  #Spliting up the words into a list for the purpose of analizing them
    returnList=[wordList,originalWordList]                      #returning everything in a list
    return (returnList)