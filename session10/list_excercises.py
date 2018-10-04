fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits index('banana', 4))  # Find next banana starting a position 4
print(fruits.reverse()) #fruits ['banana', 'apple','kiwi','banana','pear','apple', 'orange']
print(fruits.append('grape')) #fruits['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
print(fruits.sort()) #fruits['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
print(fruits.pop()) #'pear'

squares = []
for x in range(10):
    squares.append(x**2)
# squares [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
squares = list(map(lambda x: x**2, range(10)))

# [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
#Equals to:
combs = []
for x in [1,2,3]:
     for y in [3,1,4]:
         if x != y:
            combs.append((x, y))