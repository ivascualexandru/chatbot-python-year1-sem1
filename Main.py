from gspread import *
from oauth2client.service_account import ServiceAccountCredentials
from GeneralOutputFixForDisc import *
from GeneralInput import *
from GeneralInputAnalysis import *
from PokemonTweet import *
from SQLite import *
import discord
from discord.ext import commands


scope = ["https://spreadsheets.google.com/feeds",  
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive", 
        "https://www.googleapis.com/auth/spreadsheets.readonly", 
        "https://www.googleapis.com/auth/spreadsheets", 
        "https://www.googleapis.com/auth/drive.readonly"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client =authorize(creds)
ID = Type = Weight = Description = GoodAgainst = BadAgainst = False
shet1 = client.open("PDB").worksheet('sheet1')
nameList=shet1.col_values(2)
FileLenght=len(nameList)
client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready.")
#data = sheet.get_all_records()          sheet.cell(y,1).value ID, 2 Name, 3 Type 1, 4 Type 2, 5 Weight, 6 Description, 7 Good Against, 8 Bad against
def searchName(infoList):
    foundPokemons=False
    pokemonInfoList=[]
    allinfo=True                                                          #print (sheet.cell(y, 6).value)
    for i in infoList[7]:
        i=i.capitalize() 
        if i in nameList:
            cell=shet1.find(i)
            y=cell.row
            foundPokemons=True 
            if infoList[9] == True:
                a="ID: "+str(shet1.cell(y, 1).value)
                pokemonInfoList.append(a)
                allinfo=False 
            if infoList[0] == True:
                b=str(shet1.cell(y, 4).value)
                b=len(b)
                if b==False:
                    a="Type: "+str(shet1.cell(y, 3).value)
                    pokemonInfoList.append(a)
                    
                    allinfo=False 
                elif b==True :
                    a="Type1: "+str(shet1.cell(y, 3).value)
                    pokemonInfoList.append(a)
                    a="Type2: "+str(shet1.cell(y, 4).value)
                    pokemonInfoList.append(a)
                    
                    allinfo=False 
            if Weight == True:
                a="Weight: "+str(shet1.cell(y, 5).value)
                pokemonInfoList.append(a)
                
                allinfo=False 
            if Description == True:
                a="Description: "+str(shet1.cell(y, 6).value)
                pokemonInfoList.append(a)
                
                allinfo=False 
            if GoodAgainst == True:
                a="Good Against: "+str(shet1.cell(y, 7).value)
                pokemonInfoList.append(a)
                allinfo=False 
            if BadAgainst == True:
                a="Bad Against: "+str(shet1.cell(y, 8).value)
                pokemonInfoList.append(a)
                allinfo=False 
            if allinfo==True :
                a="ID: "+str(shet1.cell(y, 1).value)
                pokemonInfoList.append(a)
                b=str(shet1.cell(y, 4).value)
                b=len(b)
                if b==False:
                    a="Type: "+str(shet1.cell(y, 3).value)
                    pokemonInfoList.append(a)
                    
                    allinfo=False 
                else:
                    a="Type1: "+str(shet1.cell(y, 3).value)
                    pokemonInfoList.append(a)
                    a="Type2: "+str(shet1.cell(y, 4).value)
                    pokemonInfoList.append(a)
                a="Weight: "+str(shet1.cell(y, 5).value)
                pokemonInfoList.append(a)
                a="Description: "+str(shet1.cell(y, 6).value)
                pokemonInfoList.append(a)
                a="Good Against: "+str(shet1.cell(y, 7).value)
                pokemonInfoList.append(a)
                a="Bad Against: "+str(shet1.cell(y, 8).value)
                pokemonInfoList.append(a)

                
    returnlist=[pokemonInfoList,foundPokemons]
    return returnlist

def howManyTypePokemon(pokemonType):
    howManyFound=0
    howManyFound1=0
    columb1=shet1.col_values(3)
    columb2=shet1.col_values(4)
    a=len(columb1)-len(columb2)
    pokemonType.append("")
    for i in range(a):
        columb2.append("")
    for y in range(0,FileLenght):
        if pokemonType[0] == columb1[y] or pokemonType[0] ==  columb2[y]:
            if len(pokemonType[1])>0:
                
                if pokemonType[1] ==     columb1[y] or pokemonType[1] == columb2[y]:
                    howManyFound1=howManyFound1+1
                    
            else:
            
                howManyFound+=1
        if len(pokemonType[1])>0:
            
            howManyFound=howManyFound1
    returnlist=[howManyFound]
  
    return  returnlist

def searchType(pokemonType,numberOfPokemons):
    columb1=shet1.col_values(3)
    columb2=shet1.col_values(4)
    pokemonType.append("")
    a=len(columb1)-len(columb2)
    for i in range(a):
        columb2.append("")
    pokemonInfoList=[]
    for y in range(0,FileLenght):
        if pokemonType[0] == columb1[y] or pokemonType[0] == columb2[y]:
            if len(pokemonType[1])>0:
                if pokemonType[1]== columb1[y]or pokemonType[1]== columb2[y]:
                    numberOfPokemons-=1
                    if numberOfPokemons>=0:
                        pokemonInfoList.append(nameList[y])
                    else:
                        break
            else:
                numberOfPokemons-=1
                if numberOfPokemons>=0:
                    pokemonInfoList.append(nameList[y])
                else:
                    break
    return pokemonInfoList


def allTrue():
    pokemonNameList=[]
    for y in range(0,FileLenght):
        print(shet1.cell(y, 2).value)
        pokemonNameList.append(shet1.cell(y, 2).value)
    return pokemonNameList


@client.event
async def on_message(message):
    
    
        
       
    work=True
    question=str(message.content)
    if "$" in message.content:
        work=False
    if work==True:
        if ("news" in question) or ("News" in question):
            await message.channel.send("$" + pokemon_tweet(1))
            question="type"
        
        infoList=[]
        a=inputFunction(question)

        infoList=inputBreakdown(a[0])
        b=a[1]
        d=infoList[1]
        infoList=infoList[0]
    
        a=searchName(infoList)
        g=a[0]
        c=a[1]
        a=g
        if c==False:
    
            if infoList[8]==True:
                infoList[6]=FileLenght
        #[types0,amount1,best2,worst3,speciaType4,specialTypeRequest5,reqNumber6,wordList7,All8,number9]
            if infoList[4]==True:
                if infoList[2]==False:
                    if infoList[3]==False:
                        if infoList[1]==True:
                            a=howManyTypePokemon(infoList[5])
                        else:
                            a=searchType(infoList[5],infoList[6])
                    elif infoList[3]==True: 
                   
                        a=BestPokemon(False,infoList[6],infoList[5])
                elif infoList[2]==True:
                
                    a=BestPokemon(True,infoList[6],infoList[5])
            else:
                if infoList[0]==False:
                    if infoList[1]==False:
                        if infoList[9]==False:
                            if infoList[2]==False:
                                if infoList[3]==False:
                                    if infoList[8]==True:
                                        a=nameList
                                    else:
                                        a=[]
                                        for i in range(infoList[6]):
                                            a.append(nameList[i+1])
                    else:
                        if infoList[8]==True:
                            a=[]
                            a.append(len(nameList))
        
                                                 
        outString=outputFuncktion(a,b,infoList,c,d)
        await message.channel.send("$"+outString)
        if message.author == client.user:
            return
client.run("API_KEY")
