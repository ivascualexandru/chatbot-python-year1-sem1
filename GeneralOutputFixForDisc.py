def outputFuncktion(infoList,originalInput,extrainfo,isitapokemon,moreinfo):
    #print(moreinfo)
    if len(originalInput)==0:
        a="Please enter something"
        return a
    
    
    elif isitapokemon==True:
        a="Thats everything i found:\n"
        
        for i in range(len(infoList)):
            a=a+str(infoList[i])+" "
            if i != len(infoList)-1:
                a=a+",\n"
            else:
                a=a+"."
        return a
    
    elif extrainfo[4]==True:
        if extrainfo[1]==True:
            
            a="There is/are "+str(infoList)+" "+str(extrainfo[5])+" type pokemon"
            a=a.replace("[", "")
            a=a.replace("]", "")
            a=a.replace("'", "")
            a=a.replace(",", "")
            return a
        elif extrainfo[2]==True:
            a="These are the top "+str(extrainfo[5])+" Pokemon: "+str(infoList)
            a=a.replace("[", "")
            a=a.replace("]", "")
            a=a.replace("'", "")
            a=a.replace(",", "")
            return a
        elif extrainfo[3]==True:
            a="These are the Worst "+str(extrainfo[5])+"Pokemon: "+str(infoList)
            a=a.replace("[", "")
            a=a.replace("]", "")
            a=a.replace("'", "")
            a=a.replace(",", "")
            return a
        else:
             
            a=str(infoList)+" is/are "+str(extrainfo[5])+" type pokemon"
            a=a.replace("[", "")
            a=a.replace("]", "")
            a=a.replace("'", "")
            a=a.replace(",", "")
            return a
            
          
    #[types0,amount1,best2,worst3,speciaType4,specialTypeRequest5,reqNumber6,wordList7,All8,number9]
    
    elif extrainfo[0]==True :
        a="A "+originalInput[-1]+"'s type is/are "+str(infoList[0])+","+str(infoList[1])
    elif extrainfo[1]:
        if extrainfo[8]:
            a="there are "+str(infoList[0]-1)
            return a

        """elif isitapokemon==False:
        if len(infoList)!=0:
            for i in range(2,len(moreinfo[2])):
                print(str(moreinfo[2][i]), end =" ")
        
            print(moreinfo[2][1], end =" ")
            for i in range(len(infoList)):
                print(infoList[i], end =" ")
                if i != len(infoList)-1:
                    print(",", end =" ")
                else:
                    print(".")"""
    else:
        
        a="Sorry kid could you ask me in a diffrent way"
        return a         
