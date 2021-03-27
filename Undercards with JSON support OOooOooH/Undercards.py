import random
import copy
import os #Comment this and the below away if it breaks the program
os.system('color 0a')
import json

###-----------------------------------===============================-----------------------------------###
#-------------------------------------CURRENT NOTES AND THINGS TO DO:-------------------------------------#
###-----------------------------------===============================-----------------------------------###
"Make all points when you have to respond have ': ' at the end to not look cluttered when you type"

#-------------------------------------===============================-------------------------------------#
"Make code work with cards other than vegetoid"

#Functionise everything"

#Make GUI and design an actual thing - Quality of life features go here"
#    Make input throughout the program support any case (.lower() all the inputs or comparisons)"
"    Replace print()s with \n" 
#    Add time pauses throughout | Leave until the end otherwise you'll have to repeat it"
"    Make more spaces throughout commands and for things happening between turns so that it is more legible"
"    Make hand command display similarly to board command. Use a function for it"

"Implement attacking with selected cards"
"    Add cancelling to attack command selection sets"
"    Make attacking with a card only be allowed once each turn"
"    Stop cards being able to attack in the same turn as they were summoned"
"    Make attack check if there are any of your cards on the board - if not don't attack"
#    Make attack check if there are any of your cards on the board that can attack - if not don't attack"

#Add support for multiple of the same card - potentially via an ID assignment and then ID selection system"
#    Make ID assignments as cards are introduced into the game"
#    Make summoning compatible"
#    Make attacking compatible"
#    Make effects compatible"

"Implement game board"
"    Make board display names only"
"    Make it display formatted stats"
    
"Implement selecting card to summon"
"    Add cancelling to summon command selection sets"
"    Add comments to summon command"
"    Make summon command take gold into consideration (and take the card cost away from it)"
"    Make summon command print the board in a formatted manner not just raw dictionaries"
#    Make summon command check if you can afford to summon any of your cards - if not don't summon"
#    Make summon check if you can afford to summon a card before entering the slot selection menu"

"Implement check command to see player stats"
"    Update check command to only include your information and be formatted correctly"

"Implement mechanic to do things when the turn advances"
"    Make certain options not advance the turn and not increase gold"
"    Make turn advancement draw a card into your deck and destroy if you have a full hand"
"    Make cards with less than 1 hp (dead ones), be removed from the board"

"COMPLETE ALL THE ABOVE (except GUI aspects) - ENTER BETA STAGE"

"Implement all non-spell cards"

"Implement taunt effect"
"    Make board lists show if a card has taunt"
"    Stop player being able to attack enemy, non-taunt cards if there are enemy taunt cards in play"
"    Stop player being able to attack enemy player if there are enemy taunt cards in play"
    
"Implement armour effect"
"    Make board lists show if a card has armour"
"    Make damage dealt reduced if a card has armour"
"    Annotate armour section of attack command"
"    Add armour to card dictionaries where required"

"Stop 'X' rarity monsters from being randomly added to player decks at beginning of game"

"Implement can't attack effect"
"   Apply the trait to all relevant cards"
"   Implement the effect"
"   Make can't attack display on the board"

"Implement dodge"
"   Apply trait to relevant cards"
"   Implement the effect"
"   Reset dodged attacks count each new turn ready to start dodging again"
"   Make dodge display on the board"

"Mix dodge and armour effects to make everything work even if its all there, you know what you meant"

"Implement charge effect"
"   Apply trait to relevant cards"
"   Implement the effect"
"   Make charge display on the board"
"   Fixed incorrect charge handling"

"Implement haste effect"
"   Apply trait to relevant cards"
"   Implement effect"
"   Make haste display on the board"
"   Fixed incorrect haste handling"

"Implement ranged effect"
"   Apply trait to relevant cards"
"   Implement effect"
"   Make ranged display on the board"

"Implement candy"
"   Apply trait to relevant cards"
"   Implement effect"
"   Make ranged display on the board"

#Implement paralyzing"
#   Apply trait to relevant cards"
#   Implement effect"
#   Make ranged display on the board"

#Implement silencing
#   Apply trait to relevant cards"
#   Implement effect"
#   Make ranged display on the board"

#Implement transparency

#Implement soul effects (most occuring on a new turn)
"    Implement soul selection system"
"    Kindness"
"        Heal player on start of turn (2 HP)"
"        Heal all your cards on the board on start of turn (1 HP)"
#    Preservance
#        Damage all monsters with KR at the beggining of the opponents turn
#        Give KR to all monsters that get damaged
#    Integrity
#        Gain 1 gold for every 5 you spend (should happen at the end of the turn with a max of 2 gold rewarded)
#    Bravery
#        If you have less than 4 cards in your hand, draw until you have 4
#    Justice
#        At the end of your turn deal 1 damage to random enemy monster
#        At the end of your turn if your health is lower than the enemy's deal 1 damage to them
#    Determination
#        Give 15HP to the player instead of dying
#    Patience
#        Deal 1 damage to all paralyzed enemy monsters
#        If there are no paralyzed monsters, paralyze a random one

#Implement artifacts
#    Normal artifacts
#    Gerson's Artifacts

#Implement dust effects

#Implement magic effects

#Implement start of turn effects

#Implement end of turn effects

#Implement card specific, uncategorised effects e.g. Cactus's

#Implement future effects

#Implement turbo effects

#Implement support effect

#Implement spells
#    Kindness
#    Determination
#    Preservance
#    Patience
#    Integrity
#    Bravery
#    Justice
#    Other
###-----------------------------------------------------------------------------------------------------###

with open('cards.json', 'r') as cardFile: #Imports all card dictionaries from json file
    cards = json.load(cardFile)

selectedCard = None
'''
¦1¦2¦3¦4¦
---------
¦5¦6¦7¦8¦'''
#Calling these in an array will be <whatever you want> -1 so slot 5 will be board[4] (array index starts at 0 not 1)
slot1 = None
slot2 = None
slot3 = None
slot4 = None
slot5 = None
slot6 = None
slot7 = None
slot8 = None
board = [slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8]

player1 = {"player": 1, "health": 30, "soul": None, "gold": 1, "deck": [], "hand": []} #You for testing purposes
player2 = {"player": 2, "health": 30, "soul": None, "gold": 1, "deck": [], "hand": []} #Enemy for testing purposes

invalidAns = True
invalidAns2 = True

def printBoard():
    print("The current cards on the board are:")
    for x in range(0,8):    #1: Name | ATK:6 | HP:8/9 | Cost:7 | CAN ATK: False | TAUNT | ARMOUR:2 | CAN'T ATTACK! | CHARGE | DODGE:2 | HASTE | RANGED | CANDY
        if board[x] == None:
            print(str(x+1)+":", "Empty")
        else:
            print(str(x+1)+":", board[x]["name"], "|", "ATK:"+str(board[x]["attack"]), "|", "HP:"+str(board[x]["health"])+"/"+str(board[x]["maxHealth"]), "|", "Cost:"+str(board[x]["cost"]), "|", "CAN ATK:", str(board[x]["canAttack"]), end = "")
            if "taunt" in board[x].keys() and board[x]["taunt"] == True:
                print(" | TAUNT", end="")
            else:
                print("", end="") 
            if "armour" in board[x].keys():
                print(" |", "ARMOUR:"+str(board[x]["armour"]), end="")
            else:
                print("", end="")
            if "cantAtk" in board[x].keys() and board[x]["cantAtk"] == True:
                print(" | CAN'T ATTACK!", end="")
            else:
                print("", end="") 
            if "charge" in board[x].keys() and board[x]["charge"] == True:
                print(" | CHARGE", end="")
            else:
                print("", end="") 
            if "dodge" in board[x].keys():
                print(" |", "DODGE:"+str(board[x]["dodge"]), end="")
            else:
                print("", end="")
            if "haste" in board[x].keys() and board[x]["haste"] == True:
                print(" | HASTE", end="")
            else:
                print("", end="") 
            if "ranged" in board[x].keys() and board[x]["ranged"] == True:
                print(" | RANGED", end="")
            else:
                print("", end="") 
            if "candy" in board[x].keys() and board[x]["candy"] == True:
                print(" | CANDY", end="")
            else:
                print("", end="") 
            print()

def replaceCard(target): #You must give the full target name eg. player1["deck"] or player2["hand"] etc.
    target.remove(target[len(target)-1]) #Removes latest card added
    target.append(cards[random.randint(0,len(cards)-1)]) #Gives you another random card

def summon(targetSpace): #ONLY USED WHEN RUNNING SUMMON IN-GAME | Reference target space in array index form - if you want to put something on the first space run summon(0) not 1
    if currentPlayer["gold"] >= x["cost"]: #Checks if you have enough gold
        board[targetSpace] = copy.deepcopy(x) #Copies the stats for the selected card to the selected space but leaves the actual card stats as they are
        currentPlayer["hand"].remove(x) #Removes the card from your hand
        invalidAns2 = False
        invalidAns = False
        currentPlayer["gold"] -= x["cost"] #Takes the card cost away from your gold
        print("Slot", str(targetSpace+1), "is now taken by", board[targetSpace]["name"])
        print("You have", str(currentPlayer["gold"]), "gold remaining.")
    else:
        print("You don't have enough gold for that, it costs", str(x["cost"]), "but you only have", str(currentPlayer["gold"]), "gold.")

while invalidAns == True: #Player 1 picks soul
    answer = input("Player 1, which soul do you want to be; kindness, determination, perserverance, patience, integrity, bravery or justice: ").lower()
    if answer == "kindness" or answer == "determination" or answer == "patience" or answer == "perseverance" or answer == "integrity" or answer == "bravery" or answer == "justice":
        player1["soul"] = answer
        print("You chose", answer)
        invalidAns = False
    else:
        print("That isn't a valid soul, try again")

invalidAns = True

while invalidAns == True: #Player 2 picks soul
    answer = input("Player 2, which soul do you want to be; kindness, determination, perseverance, patience, integrity, bravery or justice: ").lower()
    if answer == "kindness" or answer == "determination" or answer == "patience" or answer == "perseverance" or answer == "integrity" or answer == "bravery" or answer == "justice":
        player2["soul"] = answer
        print("You chose", answer)
        invalidAns = False
    else:
        print("That isn't a valid soul, try again")


for x in range(26): #Gives player 1 26 random non-summon-only cards
    player1["deck"].append(cards[random.randint(0,len(cards)-1)])
    while player1["deck"][len(player1["deck"])-1]["rarity"] == "X": #Replaces card every time a summon-only card is given to you
        replaceCard(player1["deck"])

for x in range(26): #Gives player 2 26 non-summon-only random cards
    player2["deck"].append(cards[random.randint(0,len(cards)-1)])
    while player2["deck"][len(player2["deck"])-1]["rarity"] == "X": #Replaces card every time a summon-only card is given to you
        replaceCard(player2["deck"])

print("Player 1:") #This decides wether to exchange the first 3 cards you get in your hand for another random one, you can only swap each card out once
for x in range(3): #3 times
    player1["hand"].append(cards[random.randint(0, len(cards)-1)]) #Adds random card to hand
    while player1["hand"][len(player1["hand"])-1]["rarity"] == "X": #Replaces card every time a summon-only card is given to you
            replaceCard(player1["hand"])
    print(player1["hand"][x]["name"], "is card number", x+1, "that will be put in your hand.") #Tells you the card
    answer1 = input("Would you like to swap it for a different random card? Type 'yes' to do so, any other response will mean your card is kept: ")
    if answer1 == "yes":
        replaceCard(player1["hand"])
        while player1["hand"][len(player1["hand"])-1]["rarity"] == "X": #Replaces card every time a summon-only card is given to you
            replaceCard(player1["hand"])
        print("Card swapped!") 
    else:
        print("Card kept!")

print("Player 2:") #This decides wether to exchange the first 3 cards you get in your hand for another random one, you can only swap each card out once
for x in range(3): #3 times
    player2["hand"].append(cards[random.randint(0, len(cards)-1)]) #Adds random card to hand
    while player2["hand"][len(player2["hand"])-1]["rarity"] == "X": #Replaces card every time a summon-only card is given to you
            replaceCard(player2["hand"])
    print(player2["hand"][x]["name"], "is card number", x+1, "that will be put in your hand.") #Tells you the card
    answer1 = input("Would you like to swap it for a different random card? Type 'yes' to do so, any other response will mean your card is kept: ")
    if answer1 == "yes":
        replaceCard(player2["hand"])
        while player2["hand"][len(player2["hand"])-1]["rarity"] == "X": #Replaces card every time a summon-only card is given to you
            replaceCard(player2["hand"])
        print("Card swapped!")
    else:
        print("Card kept!")

advanceTurn = True
turn = 0.0
currentPlayer = 0

while player1["health"] > 0 and player2["health"] > 0: #As long as everyone is alive
    invalidAns = True
    invalidAns2 = True
    invalidAns3 = True
    
    if advanceTurn == True: #Variable used to determine whether to go to the next turn and do everything that happens on a new turn, it is usually located at the end of each option
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

    if advanceTurn == True: #EVERYTHING THAT HAPPENS ON A NEW TURN SHOULD AND WILL BE PUT INSIDE THIS LOOP AS IT IS IMPLEMENTED
        #Resets attack for every card on the board so it can attack that turn
        for x in range(0,8):
            if board[x] == None:
                pass
            else:
                if "cantAttack" in board[x].keys():
                    pass
                else:
                    board[x]["canAttack"] = True
                if "dodge" in board[x].keys():
                    board[x]["dodgedAttacks"] = 0
                else:
                    pass
                if "candy" in board[x].keys():
                    if board[x]["health"] + 3 > board[x]["maxHealth"]:
                        board[x]["health"] = board[x]["maxHealth"]
                    else:
                        board[x]["health"] += 3
                else:
                    pass
                if "haste" in board[x].keys() and board[x]["haste"] == True:
                    board[x]["haste"] = False
                else:
                    pass
                if "charge" in board[x].keys() and board[x]["charge"] == True:
                    board[x]["charge"] = False
                else:
                    pass
        if currentPlayer["soul"] == "kindness": #Heals player by 2 if kindness
            if currentPlayer["health"] + 2 > 30:
                currentPlayer["health"] = 30
            else:
                currentPlayer["health"] += 2
            if currentPlayer["player"] == 1: #Heals all their cards by 1
                for x in range(4):
                    if board[x] != None and board[x]["maxHealth"] >= board[x]["health"] + 1: #Checks if healing by 1 will exceed card's max health
                        board[x]["health"] += 1
                    else:
                        pass
            else:
                for x in range(4,8):
                    if board[x] != None and board[x]["maxHealth"] >= board[x]["health"] + 1:
                        board[x]["health"] += 1
                    else:
                        pass

        #Taking a new card
        if len(currentPlayer["hand"]) > 6:
            print("You overdrew", currentPlayer["deck"][len(currentPlayer["deck"])-1]["name"], " therefore it was destroyed!")
            currentPlayer["deck"].remove(currentPlayer["deck"][len(currentPlayer["deck"])-1]) #Actually removes the card
        else:
            #print(len(currentPlayer["deck"])) #This is for testing
            currentPlayer["hand"].append(currentPlayer["deck"][len(currentPlayer["deck"])-1]) #Check below
            currentPlayer["deck"].remove(currentPlayer["deck"][len(currentPlayer["deck"])-1]) #Puts last card in your deck into your hand (by copying from deck to hand and then deleting)
    else:
        pass

    print("\nIt is player ", currentPlayer["player"], "'s turn.")
    print("Your current hand is:")
    for x in range(len(currentPlayer["hand"])):
        print(currentPlayer["hand"][x]["name"]) #Prints out the current players full hand

    #The below changes advanceTurn back to false if it's true, ready for the next run 
    if advanceTurn == True:
        advanceTurn = False
    else:
        pass
    
    answer = input("\nWhat would you like to do? summon | attack | atkSelf | selfKill | check | hands | decks | board | endTurn: ") #Option selection interface (not really an interface but we want to seem good at this)
    print()

    if answer == "summon" and currentPlayer["player"] == 1: #Summoning for PLAYER 1!
        printBoard()
        print("\nYour currently have", str(currentPlayer["gold"]), "gold.")
        while invalidAns == True:
            print()
            card = input("Which card would you like to summon? If this appears again then you typed something wrong. Type 'cancel' to go back: ")
            for x in currentPlayer["hand"]: #Checks the
                if card == x["name"]:         #answer against
                    while invalidAns2 == True:     #each card in your hand
                        space = input("\nOnto which space on the board would you like to put this? (1-4; type 'cancel' to go back): ")
                        print()
                        if space == "1" and board[0] == None: #The comments for this if apply to all the below ones
                            summon(0)
                        elif space == "2" and board[1] == None:
                            summon(1)
                        elif space == "3" and board[2] == None:
                            summon(2)
                        elif space == "4" and board[3] == None:
                            summon(3)
                        elif space == "cancel" and invalidAns2 == True: #Exits summon command entirely
                            print("Cancelling command...\n")
                            invalidAns2 = False
                            invalidAns = False
                        else:
                            print("That space is invalid or taken!")
                            invalidAns2 = True #Keeps the loop going so that player can enter a correct answer
                elif card == "cancel" and invalidAns == True:
                    print("\nCancelling command...\n")
                    invalidAns = False
                else:
                    pass

    elif answer == "summon" and currentPlayer["player"] == 2: #Summoning for PLAYER 2!
        printBoard()
        while invalidAns == True:
            print("\n\nYour currently have", str(currentPlayer["gold"]), "gold.")
            card = input("Which card would you like to summon? If this appears again then you typed something wrong. Type 'cancel' to go back: ")
            for x in currentPlayer["hand"]: #Checks the
                if card == x["name"]:         #answer against
                    while invalidAns2 == True:     #each card in your hand
                        space = input("\nOnto which space on the board would you like to put this? (5-8); type 'cancel' to go back: ")
                        print()
                        if space == "5" and board[4] == None: #The comments for this if apply to all the below ones
                            summon(4)
                        elif space == "6" and board[5] == None:
                            summon(5)
                        elif space == "7" and board[6] == None:
                            summon(6)
                        elif space == "8" and board[7] == None:
                            summon(7)
                        elif space == "cancel" and invalidAns2 == True: #Exits summon command entirely
                            print("Cancelling command...")
                            print()
                            invalidAns2 = False
                            invalidAns = False
                        else:
                            print("That space is invalid or taken!")
                            invalidAns2 = True #Keeps the loop going so that player can enter a correct answer
                elif card == "cancel" and invalidAns == True:
                    print("\nCancelling command...\n")
                    invalidAns = False
                else:
                    pass

    elif answer == "board":
        printBoard()
    elif answer == "hands": #Prints every card in both player's hands
        print("Player 1's hand:")
        for x in player1["hand"]:
            print(x["name"])
        print("\nPlayer 2's hand:")
        for x in player2["hand"]:
            print(x["name"])

    elif answer == "attack" and currentPlayer["player"] == 1: #Attacking for Player 1 only
        for x in range(4):
            if board[x] == None:
                invalidAns = False
                noCards = True
            else:
               invalidAns = True
               noCards = False
               break
        while invalidAns == True:
            printBoard()
            atkCard = input("\nWhich card would you like to attack with (by name)? Type 'cancel' to leave the command: ")
            for x in range(0,4):
                if board[x] != None: #Had to be done in a seperate if to avoid errors for getting ["name"] of None << 1
                    if board[x]["name"] == atkCard and board[x]["canAttack"] == True:
                        print("Selected", atkCard, "as attacking card.")
                        while invalidAns2 == True:
                            target = input("\nWhich card would you like to attack (by name); type 'player' to attack the enemy player. Type 'cancel' to leave the command: ")
                            print()
                            for y in range(4,8): #Had to be filled with [invalidAns = True]s to avoid being executed one more time when exiting the whole loop
                                if board[y] != None and target == board[y]["name"] and invalidAns == True: # \/ this checks if there are taunt monsters on the enemy's board << 3
                                    if "taunt" in board[y].keys() == False and ((board[4] != None and "taunt" in board[4].keys()) or (board[5] != None and "taunt" in board[5].keys()) or (board[6] != None and "taunt" in board[6].keys())  or (board[7] != None and "taunt" in board[7].keys())):
                                        print("You can't attack this card as it isn't a taunt card and the enemy has taunt cards in on the board.")
                                    else:
                                        if "dodge" in board[y].keys() and board[y]["dodge"] >= board[y]["dodgedAttacks"]: #Dodges attack, highest priority
                                            board[y]["dodgedAttacks"]+=1
                                            print("The target card dodged your attack.")
                                        elif "armour" in board[y].keys() and board[y]["armour"] >= board[x]["attack"]: #If enemy's armour is greater than or equal to your attack nothing happens
                                            print("You dealt no damage to the enemy card because its armour was higher than your attack.")
                                        elif "armour" in board[y].keys():
                                            board[y]["health"] -= board[x]["attack"] - board[y]["armour"] #Deals reduced damage to enemy
                                            print("Your", board[x]["name"], "dealt", str(board[x]["attack"] - board[y]["armour"])+"/"+str(board[x]["attack"]), "damage to the enemy's", board[y]["name"], "as its armour negated some of the damage. It now has", str(board[y]["health"]), "HP.")
                                        else:
                                            board[y]["health"] -= board[x]["attack"] #Normal attacking
                                            print("Your", board[x]["name"], "dealt", str(board[x]["attack"]), "damage to the enemy's", board[y]["name"]+". It now has", str(board[y]["health"]), "HP.")
                                        board[x]["canAttack"] = False #Done and dealt with
                                        if "ranged" in board[x].keys():
                                            print("You received no return damage as you had the ranged effect")
                                        elif "dodge" in board[x].keys() and board[x]["dodge"] >= board[x]["dodgedAttacks"]: #You dodge atetack, highest priority
                                            print("You dodged the enemy card's returning attack damage.")
                                        elif "armour" in board[x].keys() and board[x]["armour"] >= board[y]["attack"]: #If your armour is greater than or equal to the enemy's attack nothing happens
                                            print("You received no returning damage because your armour was higher than its attack.")
                                        elif "armour" in board[y].keys(): #You receive reduced damage
                                            board[x]["health"] -= (board[y]["attack"] - board[x]["armour"])
                                            print("In return, the enemy's", board[y]["name"], "dealt", str(board[y]["attack"] - board[x]["armour"])+"/"+str(board[y]["attack"]), "damage to the your", board[x]["name"], "as its armour negated some of the damage. It now has", str(board[x]["health"]), "HP.")
                                        else:
                                            board[x]["health"] -= board[y]["attack"] #Normal return damage
                                            print("In return, the enemy's", board[y]["name"], "dealt", str(board[y]["attack"]), "damage to your", board[x]["name"]+". It now has", str(board[x]["health"]), "HP.")
                                        invalidAns = False #Exits the command
                                        invalidAns2 = False
                                        if "haste" in board[x].keys() and board[x]["haste"] == True:
                                            board[x]["haste"] = False #Removes haste from card if applicable
                                        else:
                                            pass
                                        if "charge" in board[x].keys() and board[x]["charge"] == True:
                                            board[x]["charge"] = False
                                        else:
                                            pass
                                elif target == "player" and invalidAns == True and "charge" in board[x].keys() and board[x]["charge"] == True:
                                    if (board[4] != None and "taunt" in board[4].keys()) or (board[5] != None and "taunt" in board[5].keys()) or (board[6] != None and "taunt" in board[6].keys())  or (board[7] != None and "taunt" in board[7].keys()):
                                        print("You can't attack the enemy as they have taunt cards on the board.")
                                    else:
                                        player2["health"] -= board[x]["attack"] #Actual damage dealing process
                                        print("Your", board[x]["name"], "dealt", str(board[x]["attack"]), "damage to Player 2. They now have", str(player2["health"]), "HP.")
                                        board[x]["canAttack"] = False
                                        invalidAns = False #Exits the command
                                        invalidAns2 = False
                                        if "charge" in board[x].keys() and board[x]["charge"] == True:
                                            board[x]["charge"] = False
                                        else:
                                            pass
                                        if "haste" in board[x].keys() and board[x]["haste"] == True:
                                            board[x]["haste"] = False #Removes haste from card if applicable
                                        else:
                                            pass
                                elif target == "player" and invalidAns == True and "haste" in board[x].keys() and board[x]["haste"] == True:
                                    print("You can't attack the enemy player with haste, only their cards.") #Stops you from attacking player if you have haste
                                    break
                                elif target == "player" and invalidAns == True: # cancel\/ Check:3
                                    if (board[4] != None and "taunt" in board[4].keys()) or (board[5] != None and "taunt" in board[5].keys()) or (board[6] != None and "taunt" in board[6].keys())  or (board[7] != None and "taunt" in board[7].keys()):
                                        print("You can't attack the enemy as they have taunt cards on the board.")
                                    else:
                                        player2["health"] -= board[x]["attack"] #Actual damage dealing process
                                        print("Your", board[x]["name"], "dealt", str(board[x]["attack"]), "damage to Player 2. They now have", str(player2["health"]), "HP.")
                                        board[x]["canAttack"] = False
                                        invalidAns = False #Exits the command
                                        invalidAns2 = False
                                elif target == "cancel" and invalidAns == True:
                                    invalidAns = False #Exits the command
                                    invalidAns2 = False
                                    print("Cancelling command...")
                                else:
                                    pass
                            if invalidAns == True: #Doesn't run if you triggered exiting << 2
                                print("Invalid target")
                            else:
                                pass
                    else:
                        pass
                else:
                    pass
            if atkCard == "cancel" and invalidAns == True:
                    invalidAns = False #Exits command
                    invalidAns2 = False
                    print("Cancelling command...")
            elif invalidAns == True: #Check: 2
                print("This card doesn't exist or can no longer attack this turn.")
            else:
                pass
        if noCards == True:
            print("You have no cards to attack with!")
        else:
            pass

    elif answer == "attack" and currentPlayer["player"] == 2: #Attacking for Player 2 only
        for x in range(4,8):
            if board[x] == None:
                invalidAns = False
                noCards = True
            else:
               invalidAns = True
               noCards = False
               break
        printBoard()
        while invalidAns == True:
            printBoard()
            atkCard = input("\nWhich card would you like to attack with (by name)? Type 'cancel' to leave the command: ")
            for x in range(4,8):
                if board[x] != None: #Had to be done in a seperate if to avoid errors for getting ["name"] of None << 1
                    if board[x]["name"] == atkCard and board[x]["canAttack"] == True:
                        print("Selected", atkCard, "as attacking card.")
                        while invalidAns2 == True:
                            target = input("\nWhich card would you like to attack (by name); type 'player' to attack the enemy player. Type 'cancel' to leave the command: ")
                            print()
                            for y in range(0,4): #Had to be filled with [invalidAns = True]s to avoid being executed one more time when exiting the whole loop
                                if board[y] != None and target == board[y]["name"] and invalidAns == True: # \/ this checks if there are taunt monsters on the enemy's board << 3
                                    if "taunt" in board[y].keys() == False and ((board[4] != None and "taunt" in board[4].keys()) or (board[5] != None and "taunt" in board[5].keys()) or (board[6] != None and "taunt" in board[6].keys())  or (board[7] != None and "taunt" in board[7].keys())):
                                        print("You can't attack this card as the enemy has taunt cards in on the board.")
                                    else:
                                        if "dodge" in board[y].keys and board[y]["dodge"] >= board[y]["dodgedAttacks"]: #Dodges attack, highest priority
                                            board[y]["dodgedAttacks"]+=1
                                            print("The target card dodged your attack.")
                                        elif "armour" in board[y].keys() and board[y]["armour"] >= board[x]["attack"]: #If enemy's armour is greater than or equal to your attack nothing happens
                                            print("You dealt no damage to the enemy card because its armour was higher than your attack.")
                                        elif "armour" in board[y].keys():
                                            board[y]["health"] -= board[x]["attack"] - board[y]["armour"] #Deals reduced damage to enemy
                                            print("Your", board[x]["name"], "dealt", str(board[x]["attack"] - board[y]["armour"])+"/"+str(board[x]["attack"]), "damage to the enemy's", board[y]["name"], "as its armour negated some of the damage. It now has", str(board[y]["health"]), "HP.")
                                        else:
                                            board[y]["health"] -= board[x]["attack"] #Normal attacking
                                            print("Your", board[x]["name"], "dealt", str(board[x]["attack"]), "damage to the enemy's", board[y]["name"]+". It now has", str(board[y]["health"]), "HP.")
                                        board[x]["canAttack"] = False #Done and dealt with
                                        if "dodge" in board[x].keys and board[x]["dodge"] >= board[x]["dodgedAttacks"]: #You dodge atetack, highest priority
                                            print("You dodged the enemy card's returning attack damage.")
                                        elif "armour" in board[x].keys() and board[x]["armour"] >= board[y]["attack"]: #If your armour is greater than or equal to the enemy's attack nothing happens
                                            print("You received no returning damage because your armour was higher than its attack.")
                                        elif "armour" in board[y].keys(): #You receive reduced damage
                                            board[x]["health"] -= (board[y]["attack"] - board[x]["armour"])
                                            print("In return, the enemy's", board[y]["name"], "dealt", str(board[y]["attack"] - board[x]["armour"])+"/"+str(board[y]["attack"]), "damage to the your", board[x]["name"], "as its armour negated some of the damage. It now has", str(board[x]["health"]), "HP.")
                                        else:
                                            board[x]["health"] -= board[y]["attack"] #Normal return damage
                                            print("In return, the enemy's", board[y]["name"], "dealt", str(board[y]["attack"]), "damage to your", board[x]["name"]+". It now has", str(board[x]["health"]), "HP.")
                                        invalidAns = False #Exits the command
                                        invalidAns2 = False
                                        if "haste" in board[x].keys() and board[x]["haste"] == True:
                                            board[x]["haste"] = False #Removes haste from card if applicable
                                        else:
                                            pass
                                        if "charge" in board[x].keys() and board[x]["charge"] == True:
                                            board[x]["charge"] = False
                                        else:
                                            pass
                                elif target == "player" and invalidAns == True and "charge" in board[x].keys() and board[x]["charge"] == True:
                                    if (board[4] != None and "taunt" in board[4].keys()) or (board[5] != None and "taunt" in board[5].keys()) or (board[6] != None and "taunt" in board[6].keys())  or (board[7] != None and "taunt" in board[7].keys()):
                                        print("You can't attack the enemy as they have taunt cards on the board.")
                                    else:
                                        player2["health"] -= board[x]["attack"] #Actual damage dealing process
                                        print("Your", board[x]["name"], "dealt", str(board[x]["attack"]), "damage to Player 2. They now have", str(player2["health"]), "HP.")
                                        board[x]["canAttack"] = False
                                        invalidAns = False #Exits the command
                                        invalidAns2 = False
                                        if "charge" in board[x].keys() and board[x]["charge"] == True:
                                            board[x]["charge"] = False
                                        else:
                                            pass
                                elif target == "player" and invalidAns == True and "haste" in board[x].keys() and board[x]["haste"] == True:
                                    print("You can't attack the enemy player with haste, only their cards.") #Stops you from attacking player if you have haste
                                    break
                                elif target == "player" and invalidAns == True: # \/ Check:3
                                    if (board[4] != None and "taunt" in board[4].keys()) or (board[5] != None and "taunt" in board[5].keys()) or (board[6] != None and "taunt" in board[6].keys())  or (board[7] != None and "taunt" in board[7].keys()):
                                        print("You can't attack the enemy as they have taunt cards on the board.")
                                    else:
                                        player2["health"] -= board[x]["attack"] #Actual damage dealing process
                                        print("Your", board[x]["name"], "dealt", str(board[x]["attack"]), "damage to Player 2. They now have", str(player2["health"]), "HP.")
                                        board[x]["canAttack"] = False
                                        invalidAns = False #Exits the command
                                        invalidAns2 = False
                                elif target == "cancel" and invalidAns == True:
                                    invalidAns = False #Exits the command
                                    invalidAns2 = False
                                    print("Cancelling command...")
                                else:
                                    pass
                            if invalidAns == True: #Doesn't run if you triggered exiting << 2
                                print("Invalid target")
                            else:
                                pass
                    else:
                        pass
                else:
                    pass
            if atkCard == "cancel" and invalidAns == True:
                    invalidAns = False #Exits command
                    invalidAns2 = False
                    print("Cancelling command...")
            elif invalidAns == True: #Check: 2
                print("This card doesn't exist or can no longer attack this turn.")
            else:
                pass
        if noCards == True:
            print("You have no cards to attack with!")
        else:
            pass

    elif answer == "decks":
        print("Player 1's Deck:")
        for x in player1["deck"]: #Prints every card in player 1's deck
            print(x["name"])
        print("\nPlayer 2's Deck:")
        for x in player2["deck"]:
            print(x["name"])

    #elif answer == "atkSelf" and vegetoid["alive"] == True: #OBSOLETE NEEDS UPDATING
    #    vegetoid["health"] -= vegetoid["attack"]

    elif answer == "selfKill": #Basically suicide ¯\_( ͡° ͜ʖ ͡°)_/¯
        currentPlayer["health"] = 0
        print("What a shame...")
        time.sleep(3)

    elif answer == "check": #Gives you all the player stats
        print("Current player stats are:", "HP:", str(currentPlayer["health"])+"/30", "|", "Gold:", str(currentPlayer["gold"]))

    elif answer == "endTurn":
        advanceTurn = True
        print("Ending turn...")

    # ! ! ! ADD ADITIONAL OPTIONS ABOVE THIS LINE ! ! !

    #elif vegetoid["alive"] == False: #If you select an option that needs vegetoid to be alive and he's dead, it runs this
    #    print("Can't do that with a dead card!") #Obsolete and irrelevant
    #    chance = random.randint(1, 50)
    #    if chance == 32:
    #        print("I know it's a big plot twist that dead things can't do things made for the living things") #I could use a multi line print but I'll probably seperate this with time.sleep()s so leave it!
    #        print("That is, in essence, the thing that makes this whole thing work")
    #        print("Things are different now after all, not the same things as things once were")
    #        print("Things these days, can't even use the word properly because everything uses it in every sentence for every meaning, why does thing have to be the thing you put in your sentence?!")
    #        print("I'll take my things and go do things that involve contemplating things somewhere else")
    #else:
    #   print("Invalid Command!")
    
    #if vegetoid["alive"] == False and vegetoid["dustTriggered"] == False: #OBSOLETE NEEDS UPDATING
    #    player1["health"] += vegetoid["healOnDeath"]
    #    print("You have been healed by " + str(vegetoid["healOnDeath"]) + "hp!")
    #    vegetoid["dustTriggered"] = True
    #else:
    #   pass

    for x in range(0,8): #Any cards with less than one HP are declared dead, board space is cleared
        if board[x] != None:
            if "charge" in board[x].keys() and board[x]["charge"] == True: #The card can attack on the first turn
                board[x]["canAttack"] = True
            else:
                pass
            if "haste" in board[x].keys() and board[x]["haste"] == True:
                board[x]["canAttack"] = True #Allows attacking, stopping the direct attacking of the enemy player is embedded within attack command
            else:
                pass
            if board[x]["health"] < 1:
                print(board[x]["name"], "has died.")
                board[x] = None
            else:
                pass
        else:
            pass
    # ! ! ! ADD DUST EFFECTS BELOW THE ABOVE LOOP OTHERWISE THEY'LL EXECUTE EVEN IF THE CARD DIED THAT TURN ! ! !
    if player1["health"] > 30: #Keeps max health at 30
        player1["health"] = 30
        print("Your health went over 30hp so was taken back down to the max value of 30hp")
    else:
        pass
    
    if player2["health"] > 30: #Keeps health at max 30
        player2["health"] = 30
        print("The enemy's health went over 30hp so was taken back down to the max value of 30hp")
    else:
        pass
    
if player1["health"] < 1:
    print("You have died! :<")
else:
    print("Your enemy has died")
