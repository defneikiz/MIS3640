#Lists

#list is a sequence

AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
numbers = [42, 123]
empty = []
# print(AFC_east, numbers, empty)

#list is mutable
#This means, we can replace, any item with another in a list. 
# Below we replaced New York Jets with New York Giants
AFC_east[3] = 'New York Giants' 
print(AFC_east)
print(AFC_east[3])

#Excercise 1
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']    
]
print(L[0][0]) #apple
print(L[2][-1]) #lisa
print(L[1][2][1]) #on rail

#Traversing a list

for team in AFC_east:
    print(team)

numbers = [2,0,1,6,9]

for i in range (len(numbers)):
    numbers[i] = numbers [i] * 2
    print(numbers)

#list operations

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
# print(c) #[1,2,3,4,5,6]

# print([0] * 4) #[0,0,0,0]

# print (['Tom Brady', 'Bill Belichick'] * 3)

#list slices

t = ['a', 'b', 'c', 'd', 'e', 'f']

t[1:3] = ['x', 'y']
# print(t)

#list methods
#Excercise02

t = ['a', 'b', 'c']
print(t.append('d')) #none
print(t.extend('d')) #none
print(t.sort()) #none