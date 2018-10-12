""" Notes and examples from 'automate the boring stuff'
"""

spam = ['jobbies','babysick','catpiss','an old man`s toenails']
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

message = 'Fuck you, you complete and utter bag of cat piss. The thought of simply having to look at your face fills me with such existential dread, that I would consider gouging out my eyeballs to avoid it'

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

for i in range(9):
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