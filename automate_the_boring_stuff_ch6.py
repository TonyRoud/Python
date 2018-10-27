""" Notes and excercises from 'automate the boring stuff'
    Chapter 6
"""

# String methods for validating input
def getAge():
    while True:
        print('Enter your age:')
        age = input()
        if age.isdecimal():
            break
        print('Please enter a number for your age. Try again.')
    print('You are ', age, 'years old? You don\'t look a day over', int(age)-1)

def getPass():
    while True:
        print('Select a new password (letters and numbers only!):')
        password = input()
        if password.isalnum():
            break
        print('passwords can only include numbers and letters. Try again.')
    print('Ok, your new password has been set to', password, 'I promise not to tell anyone!')

# Methods for fomulating tabular data
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth), '-')
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)