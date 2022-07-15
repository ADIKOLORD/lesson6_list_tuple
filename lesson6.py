dafafafdd
"""
db = ['alf', 'fjadsk', 3, 4, 5, 65, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
while True:
    for i in db:
        if i == 1:
            db.remove(i)
    if 1 not in db:
        break
print(db)
"""

"""
# Problem 3
names = ['Aktilek', 'Kalybek', 'Rasul']
empty = ' '
empty = empty.join(names)
print(empty)

# Problem 4
l1 = ['adsf', 2, 3, 'af', [2, 'hello', True], (1, 3,)]
l2 = [2, 3.3, 'adfad', True]
print(l1 + l2)

# Problem 5
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
print(names.count('Jack'))

# Problem 6
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon', 'Jimmy', 'Jackson', 'Jhon', 'Jack', 'Jimmy', 'Jack',
         'Jackson', 'Jhon', 'Jackson', 'Jhon', 'Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', ]
for i in names:
    if i == 'Oskar':
        names.remove(i)

# Problem 7
empty_list = []
empty_list.append('Adilet')
empty_list.append(2004)
empty_list.append('Python( других не знаю просто :) )')
print(empty_list)

# Problem 8
pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
print(pythonList.index('loop'))

# Problem 9
numbers = [123, 321, 2, 543, 64, 463, 234, 867, 6234, 63246, 3, 43]
pro = 1
for i in numbers:
    pro *= i
print(pro)  # >= 13110687350904927811539852288


# Problem 10
word = 'itcbootcamp123course3445'
number = []
letter = []
for i in word:
    try:
        number.append(int(i))
    except ValueError:
        letter.append(i)

print(number, letter, sep='\n')


# Problem 11
pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
print(pythonList[1:4])


# Second variant Problem 10

letter = []
number = []
word = 'itcbootcamp123course3445'
for i in word:
    if i not in '1234567890':
        letter.append(i)
    else:
        number.append(int(i))
print(number)
print(letter)

#########

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0], numbers[-1], numbers[4])


# Palindrom
words = ['Anna', 'Civic', 'Kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]
palindrom = []
for i in words:
    if i.lower() == i[::-1].lower():
        palindrom.append(i)
print(palindrom)


# Number 3
list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
general = []
for i in list_1:
    if i in list_2:
        general.append(i)
print(general)


"""













