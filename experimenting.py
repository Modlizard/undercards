import datetime
import time
import random
import copy
import os #Comment this and the below away if it breaks the program
os.system('color 0a')

#----------------------------------------------------
#Current notes and things to do:
#Make code work with cards other than vegetoid !
#Implement spells
"Implement game board"
"Implement selecting card to summon"
#Add cancelling to summon command selection sets !!!
#Make board display names only !!!
#Add comments to summon command !!!
"Make certain options not advance the turn and not increase gold"
#----------------------------------------------------

#experimental
#RAW COPYING FORMAT BELOW
#= {"name": "!", "attack": %, "health": $, "cost": ^, "rarity": "@", "alive": True}
#Rarity Key: S - starter; C - common;  R - rare; E - epic; D - DT; X - summon only
bun = {"name": "Bun", "attack": 1, "health": 1, "cost": 0, "rarity": "X", "alive": True}
gift = {"name": "Gift", "attack": 0, "health": 2, "cost": 0, "rarity": "X", "alive": True}
tinyFroggit = {"name": "Tiny Froggit", "attack": 1, "health": 1, "cost": 0, "rarity": "C", "alive": True}
blueSnail = {"name": "Blue Snail", "attack": 1, "health": 1, "cost": 1, "rarity": "C", "alive": True}
chest = {"name": "Chest", "attack": 0, "health": 3, "cost": 1, "rarity": "C", "alive": True}
cleanRabbick = {"name": "Clean Rabbick", "attack": 1, "health": 1, "cost": 1, "rarity": "X", "alive": True}
dummy = {"name": "Dummy", "attack": 0, "health": 4, "cost": 1, "rarity": "S", "alive": True}
greenFlower = {"name": "Green Flower", "attack": 1, "health": 1, "cost": 1, "rarity": "X", "alive": True}
lancerPainting = {"name": "Lancer Painting", "attack": 1, "health": 1, "cost": 1, "rarity": "C", "alive": True}
pebble = {"name": "Pebble", "attack": 1, "health": 3, "cost": 1, "rarity": "X", "alive": True}
redSnail = {"name": "Red Snail", "attack": 1, "health": 1, "cost": 1, "rarity": "C", "alive": True}
snowman = {"name": "Snowman", "attack": 1, "health": 2, "cost": 1, "rarity": "C", "alive": True}
spider = {"name": "Spider", "attack": 2, "health": 1, "cost": 1, "rarity": "C", "alive": True}
yellowSnail = {"name": "Yellow Snail", "attack": 1, "health": 1, "cost": 1, "rarity": "C", "alive": True}
annoyingDog = {"name": "Annoying Dog", "attack": 2, "health": 3, "cost": 2, "rarity": "R", "alive": True}
bloodyTree = {"name": "Bloody Tree", "attack": 2, "health": 1, "cost": 2, "rarity": "C", "alive": True}
bridgeSeed = {"name": "Bridge Seed", "attack": 0, "health": 2, "cost": 2, "rarity": "C", "alive": True}
charles = {"name": "Charles", "attack": 2, "health": 2, "cost": 2, "rarity": "C", "alive": True}
dogResidue = {"name": "Dog Residue", "attack": 1, "health": 2, "cost": 2, "rarity": "X", "alive": True}
doodlebog = {"name": "Doodlebog", "attack": 2, "health": 2, "cost": 2, "rarity": "X", "alive": True}
fanRudinn = {"name": "Fan Rudinn", "attack": 1, "health": 1, "cost": 2, "rarity": "C", "alive": True}
flowerJar = {"name": "Flower Jar", "attack": 2, "health": 2, "cost": 2, "rarity": "C", "alive": True}
froggit = {"name": "Froggit", "attack": 2, "health": 3, "cost": 2, "rarity": "S", "alive": True}
gFollower1 = {"name": "G Follower 1", "attack": 3, "health": 1, "cost": 2, "rarity": "C", "alive": True}
lamp = {"name": "Lamp", "attack": 0, "health": 1, "cost": 2, "rarity": "C", "alive": True}
leftTentacle = {"name": "Left Tentacle", "attack": 1, "health": 3, "cost": 2, "rarity": "X", "alive": True}
loox = {"name": "Loox", "attack": 2, "health": 2, "cost": 2, "rarity": "S", "alive": True}
lostSoul3 = {"name": "Lost Soul 3", "attack": 1, "health": 1, "cost": 2, "rarity": "X", "alive": True}
mettabot = {"name": "Mettabot", "attack": 1, "health": 1, "cost": 2, "rarity": "X", "alive": True}
migosp = {"name": "Migosp", "attack": 2, "health": 2, "cost": 2, "rarity": "S", "alive": True}
moldsmal = {"name": "Modldsmal", "attack": 3, "health": 2, "cost": 2, "rarity": "S", "alive": True}
monsterKid = {"name": "Monster Kid", "attack": 2, "health": 2, "cost": 2, "rarity": "R", "alive": True}
ragel = {"name": "Ragel", "attack": 3, "health": 2, "cost": 2, "rarity": "U", "alive": True}
rightTentacle = {"name": "Right Tentacle", "attack": 3, "health": 1, "cost": 2, "rarity": "X", "alive": True}
rudinn = {"name": "Rudinn", "attack": 1, "health": 3, "cost": 2, "rarity": "C", "alive": True}
temmie = {"name": "Temmie", "attack": 2, "health": 1, "cost": 2, "rarity": "R", "alive": True}
worm = {"name": "Worm", "attack": 1, "health": 3, "cost": 2, "rarity": "X", "alive": True}
allergicTemmie = {"name": "Allergic Temmie", "attack": 2, "health": 2, "cost": 3, "rarity": "R", "alive": True}
bigBob = {"name": "Big Bob", "attack": 2, "health": 3, "cost": 3, "rarity": "R", "alive": True}
bomb = {"name": "Bomb", "attack": 1, "health": 6, "cost": 3, "rarity": "C", "alive": True}
vegetoid = {"health": 3, "attack": 3, "healOnDeath": 3, "dustTriggered": False, "alive": True}

cards = [bun, gift, tinyFroggit, blueSnail, chest, cleanRabbick, dummy, greenFlower, lancerPainting, pebble, redSnail, snowman, spider, yellowSnail, annoyingDog, bloodyTree, bridgeSeed, charles, dogResidue, doodlebog, fanRudinn, flowerJar, froggit, gFollower1, lamp, leftTentacle, loox, lostSoul3, mettabot, migosp, moldsmal, monsterKid, ragel, rightTentacle, rudinn, temmie, worm, allergicTemmie, bigBob, bomb]

deckP1 = []
deckP2 = []
handP1 = []
handP2 = []
selectedCard = None
'''
¦1¦2¦3¦4¦
---------
¦5¦6¦7¦8¦
'''
#Calling these in an array will be -1 so slot 1 will be board[0]
slot1 = None
slot2 = None
slot3 = None
slot4 = None
slot5 = None
slot6 = None
slot7 = None
slot8 = None
board = [slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8]

for x in range(27): #Gives player 1 26 random cards
    deckP1.append(cards[random.randint(0,len(cards)-1)])

for x in range(27): #Gives player 2 26 random cards
    deckP2.append(cards[random.randint(0,len(cards)-1)])

print("Player 1:") #This decides wether to exchange the first 3 cards you get in your hand for another random one, you can only swap each card out once
for x in range(3): #3 times
    handP1.append(cards[random.randint(0, len(cards)-1)]) #Adds random card to hand
    print(handP1[x]["name"], "is card number", x+1, "that will be put in your hand.") #Tells you the card
    answer1 = input("Would you like to swap it for a different random card? Type 'yes' to do so, any other response will mean your card is kept")
    if answer1 == "yes":
        handP1.remove(handP1[len(handP1)-1]) #Removes latest card given (this one)
        handP1.append(cards[random.randint(0, len(cards)-1)]) #Gives you another random card
        print("Card swapped!")
    else:
        print("Card kept!")

print("Player 2:") #This decides wether to exchange the first 3 cards you get in your hand for another random one, you can only swap each card out once
for x in range(3): #3 times
    handP2.append(cards[random.randint(0, len(cards)-1)]) #Adds random card to hand
    print(handP2[x]["name"], "is card number", x+1, "that will be put in your hand.") #Tells you the card
    answer1 = input("Would you like to swap it for a different random card? Type 'yes' to do so, any other response will mean your card is kept")
    if answer1 == "yes":
        handP2.remove(handP2[len(handP2)-1]) #Removes latest card given (this one)
        handP2.append(cards[random.randint(0, len(cards)-1)]) #Gives you another random card
        print("Card swapped!")
    else:
        print("Card kept!")

player1 = {"player": 1, "health": 30, "soul": None, "gold": 1, "deck": deckP1, "hand": handP1} #You for testing purposes
player2 = {"player": 2, "health": 30, "soul": None, "gold": 1, "deck": deckP2, "hand": handP2} #Enemy for testing purposes

invalid = True
invalid2 = True
advanceTurn = True
turn = 0.0
currentPlayer = 0
while player1["health"] > 0 and player2["health"] > 0:

    invalid = True
    invalid2 = True
    
    if advanceTurn == True: #Variable used to determine wether to go to the next turn and do everything that happens on a new turn, it is usually located at the end of each option
        turn += 1.0
    else:
        pass
    
    #The below don't require advanceTurn as the turn itself is already changed/left alone
    if (turn/2.0).is_integer(): #Odd turn means it's player 1's turn even means player 2's
        currentPlayer = player2
    else:
        currentPlayer = player1
        
    #The below doesn't execute if it is not the next turn
    if turn < 21 and advanceTurn == True: #First and second turn give +1g, 3 and 4 give +2g, 5 and 6 give +3g etc.
        currentPlayer["gold"] += round(turn/2.0)
    elif advanceTurn == True: #To avoid earning more than 10g in one turn you just receive 10 after turn 21
        currentPlayer["gold"] += 10
    else:
        pass
    
    #The below changes advanceTurn back to false if it's true ready for the next run 
    if advanceTurn == True:
        advanceTurn = False
    else:
        pass

    print("It is player ", currentPlayer["player"], "'s turn.")
    print("Your current hand is:")
    for x in range(len(currentPlayer["hand"])):
        print(currentPlayer["hand"][x]["name"]) #Prints out the current players full hand

    answer = input("What would you like to do? summon | atkEnemy | atkSelf | selfKill | check | decks | board") #Option selection interface (not really an interface but we want to seem good at this)
    if answer == "summon" and currentPlayer["player"] == 1:
        print("The current cards on your board are (slots 1-4):", board[0], board[1], board[2], board[3])
        while invalid == True:
            answer3 = input("Which card would you like to summon? If this appears again then you typed something wrong.")
            for x in currentPlayer["hand"]:
                if answer3 == x["name"]:
                    while invalid2 == True:
                        answer4 = input("Onto which space on the board would you like to put this? (1-4)")
                        if answer4 == "1" and board[0] == None:
                            board[0] = copy.deepcopy(x)
                            currentPlayer["hand"].remove(x)
                            invalid2 = False
                            invalid = False
                            print("Slot 1 now is now taken by", board[0]["name"])
                        elif answer4 == "2" and board[1] == None:
                            board[1] = copy.deepcopy(x)
                            currentPlayer["hand"].remove(x)
                            invalid2 = False
                            invalid = False
                            print("Slot 2 now is now taken by", board[1]["name"])
                        elif answer4 == "3" and board[2] == None:
                            board[2] = copy.deepcopy(x)
                            currentPlayer["hand"].remove(x)
                            invalid2 = False
                            invalid = False
                            print("Slot 3 now is now taken by", board[2]["name"])
                        elif answer4 == "4" and board[3] == None:
                            board[3] = copy.deepcopy(x)
                            currentPlayer["hand"].remove(x)
                            invalid2 = False
                            inavlid = False
                            print("Slot 4 now is now taken by", board[3]["name"])
                        else:
                            print("That space is invalid or taken!")
                            invalid2 = True
                else:
                    pass
    elif answer == "summon" and currentPlayer["player"] == 2:
        print("The current cards on your board are (slots 5-8):", board[4], board[5], board[6], board[7])
        while invalid == True:
            answer3 = input("Which card would you like to summon? If this appears again then you typed something wrong.")
            for x in currentPlayer["hand"]:
                if answer3 == x["name"]:
                    while invalid2 == True:
                        answer4 = input("Onto which space on the board would you like to put this? (5-8)")
                        if answer4 == "5" and board[4] == None:
                            board[4] = copy.deepcopy(x)
                            currentPlayer["hand"].remove(x)
                            invalid2 = False
                            invalid = False
                            print("Slot 5 now is now taken by", board[4]["name"])
                        elif answer4 == "6" and board[5] == None:
                            board[5] = copy.deepcopy(x)
                            currentPlayer["hand"].remove(x)
                            invalid2 = False
                            invalid = False
                            print("Slot 6 now is now taken by", board[5]["name"])
                        elif answer4 == "7" and board[6] == None:
                            board[6] = copy.deepcopy(x)
                            currentPlayer["hand"].remove(x)
                            invalid2 = False
                            invalid = False
                            print("Slot 7 now is now taken by", board[6]["name"]) 
                        elif answer4 == "8" and board[7] == None:
                            board[7] = copy.deepcopy(x)
                            currentPlayer["hand"].remove(x)
                            invalid2 = False
                            invalid = False
                            print("Slot 8 now is now taken by", board[7]["name"])
                        else:
                            print("That space is invalid or taken!")
                            invalid2 = True
                else:
                    pass
    elif answer == "board":
        for x in board:
            print(x)
    elif answer == "atkEnemy" and vegetoid["alive"] == True:
        player2["health"] -= vegetoid["attack"]
        print("Enemy damaged, current health is " + str(player2["health"]) + "HP!")
    elif answer == "decks":
        print("Player 1's Deck:")
        for x in deckP1:
            print(x["name"])
        print()
        print("Player 2's Deck:")
        for x in deckP2:
            print(x["name"])
    elif answer == "atkSelf" and vegetoid["alive"] == True:
        vegetoid["health"] -= vegetoid["attack"]
    elif answer == "selfKill":
        player1["health"] = 0
        print("What a shame...")
    elif answer == "check":
        print("Enemy health is ", str(player2["health"]), "HP, their gold is ", str(player2["gold"]), ", your health is ", str(player1["health"]) + "HP, your gold is ", str(player1["gold"]), ", card attack is " + str(vegetoid["attack"]) + ", card health is " + str(vegetoid["health"]) + "hp.")
    # ! ! ! ADD ADITIONAL OPTIONS ABOVE THIS LINE ! ! !
    elif vegetoid["alive"] == False: #If you select an option that needs vegetoid to be alive and he's dead, it runs this
        print("Can't do that with a dead card!")
        chance = random.randint(1, 50)
        if chance == 32:
            print("I know it's a big plot twist that dead things can't do things made for the living things")
            print("That is, in essence, the thing that makes this whole thing work")
            print("Things are different now after all, not the same things as things once were")
            print("Things these days, can't even use the word properly because everything uses it in every sentence for every meaning, why does thing have to be thing you put in your sentence?!")
            print("I'll take my things and go do things that involve contemplating things somewhere else")
    else:
        print("Invalid Command!")
    
    if vegetoid["health"] < 1:
        vegetoid["alive"] = True
        print("Your card is dead!")
    else:
        pass
    
    if vegetoid["alive"] == False and vegetoid["dustTriggered"] == False:
        player1["health"] += vegetoid["healOnDeath"]
        print("You have been healed by " + str(vegetoid["healOnDeath"]) + "hp!")
        vegetoid["dustTriggered"] = True
    else:
        pass

    if player1["health"] > 30:
        player1["health"] = 30
        print("Your health went over 30hp so was taken back down to the max value of 30hp")
    else:
        pass
    
    if player2["health"] > 30:
        player2["health"] = 30
        print("The enemy's health went over 30hp so was taken back down to the max value of 30hp")
    else:
        pass
    
if player1["health"] < 1:
    print("You have died! :<")
else:
    print("Your enemy has died")
