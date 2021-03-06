""" Notes and excercises from 'automate the boring stuff'
"""

spam = ['ham','eggs','chips','bacon']
message = ""

for x in range(0, (len(spam) - 1)):
    message += spam[x] + ', '

message = message + ' and ' + spam[-1]

print(message)

###########################################

grid = [['.','.','.','.','.','.','.'],
        ['.','0','0','.','.','.','.'],
        ['0','0','0','0','.','.','.'],
        ['0','0','0','0','0','0','.'],
        ['.','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','.'],
        ['0','0','0','0','.','.','.'],
        ['.','0','0','.','.','.','.'],
        ['.','.','.','.','.','.','.']]

output = ""

for x in range(0, len(grid[0])):
    output = ""
    for y in range(0, len(grid)):
        output = output + grid[y][x]
    print(output)

###########################################

spam = {'colour':'red', 'age':'42'}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

###########################################

import pprint

message = 'Listen here you litte'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

###########################################

theBoard = {'top-L':' ', 'top-M':' ', 'top-R':' ',
            'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
            'low-L':' ', 'low-M':' ', 'low-R':' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'

for i in range(12):
    printBoard(theBoard)
    print('Turn for player ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn =='X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)

###########################################

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches' : 3, 'apples' : 2},
             'Carol': {'Cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))

###########################################
"""
Function to list adventurer's inventory, including total
"""
inventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}

def displayinventory(inventory):
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v
        print(str(v) + " " + str(k))
    print("Total number of items: " + str(item_total))

displayinventory(inventory)

#############################################

"""
Function to add an inventory of a dragon
to the adventurer's existing inventory
"""
def addToInventory(inventory, addedItems):
    # initialise total items variable, to increment each time
    for k in addedItems:
        if inventory.get(k, 0) > 0:
            inventory[k] = inventory[k] + 1
        else:
            inventory.setdefault(k, 1)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
displayinventory(inv)