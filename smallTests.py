'''arr = ["Steve", "Jim", "Lewis"]
arr.append("Jeremy")
print(arr)'''

'''arr1 = ["Steve", "Jim", "Lewis"]
arr2 = ["Alpha", "Beta", "Gamma"]
dictionary1 = {"one": arr1, "two": arr2}
print(dictionary1["one"][1])'''

'''arr1 = ["Steve", "Jim", "Lewis"]
arr1.remove(arr1[len(arr1)-1])
print(arr1)'''

'''answ = input("y/n?")
if answ == "y":
    print("yes")
elif answ == "n":
    print("no")
else:
    print("invalid command")
    return'''

'''arr1 = ["Steve", "Jim", "Lewis"]
print(arr1)
arr1.append("ree")
print(arr1)'''

'''x = "chicken"
print(x + "1")
print(x, "2")
print(x,"3")
#comma automatically adds a space'''

'''arr = ["Steve", "Jim", "Lewis"]
for x in arr:
    print(x)'''

'''for x in range(2):
    print(str(x))'''

'''bun = {"name": "Bun", "attack": 1, "health": 5, "maxHealth": 5, "cost": 0, "rarity": "X", "alive": True}
x = 3
bun["health"] -= (x - bun["armour"])
print(str(bun["health"]))'''

'''bun = {"name": "Bun", "attack": 1, "health": 5, "maxHealth": 5, "cost": 0, "rarity": "X", "alive": True}
print(bun.keys())
'''

#Use to check if certain key in dicitionary exists
'''bun = {"name": "Bun", "attack": 1, "health": 5, "maxHealth": 5, "cost": 0, "rarity": "X", "alive": True, "taunt": True}
if "taunt" in bun.keys():
    print("Has taunt")
else:
    print("Rip that enemy guy")'''

'''board = [None, None, None, None, None, None, None]
board[4] = {"name": "Bun", "attack": 1, "health": 5, "maxHealth": 5, "cost": 0, "rarity": "X", "alive": True, "canAttack": True, "taunt": True}
board[2] = {"name": "Run", "attack": 5, "health": 2, "maxHealth": 3, "cost": 0, "rarity": "X", "alive": True, "canAttack": True}
for x in range(0,7):    #1: Name | ATK:6 | HP:8/9 | Cost:7 | Can Attack: False
            if board[x] == None:
                print(str(x+1)+":", "Empty")
            else:
                print(str(x+1)+":", board[x]["name"], "|", "ATK:"+str(board[x]["attack"]), "|", "HP:"+str(board[x]["health"])+"/"+str(board[x]["maxHealth"]), "|", "Cost:"+str(board[x]["cost"]), "|", "Can Attack:", str(board[x]["canAttack"]), end = "")
                if "taunt" in board[x].keys():
                    print(" |", "TAUNT")
                else:
                    print("")
'''

'''test = None
test2 = {"t": "ree", "noot": 4}
if (test != None and "taunt" in test.keys()):
    print("true")
else:
    print("falsE")

print(str("taunt" in test2.keys()))'''

alpha = {'a': True, 'b': False}
beta = {'c': False, 'd': False}
omega = [alpha,beta]
print(str(len(omega)))
