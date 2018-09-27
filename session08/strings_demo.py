# team= 'New England Patriots'
# letter= team[1] #the expression in brackets is called an indez
# print(letter)
# #gives e, because index 1 refers to 2nd letter in coding

# len(team)

# print(team[0])

# team[20-1] #s
# team[len(team)-1] #s
# team[-1] #s

# for letter in team:
#     print(letter)

# prefixes= 'JKLMNOPQ'
# suffix= 'ack'
# for letter in prefixes:
#     if letter== 'O' or letter == 'Q':
#         print(letter +'u'+suffix)
#     else:
#         print(letter + suffix)
team= 'New England Patriots'
# print(team[0:11]) #New England same as [:11] regular counting
# print(team[12:20])
# # print(team[11:4]) you get '' because there is no index 4 after 11
# print(team[0:20:2]) #NwEgadPtit , same as [::2]
# print(team[::-2]) #goes reverse 'sora nln e'

# #Search
# def find(word,letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index +1
#     return -1

# for i in range (len(team)):
#     if team [i] == 'a':
#         print(i)
#alternative for loop
# for i, letter in enumerate(team): #traverse the whole collection we can get both index and value of element
#     print(i,letter)

#counter
word='New England Patriots'
count=0
# for letter in word:
#     if letter == 'a':
#         count= count +1 # adds one each time it encounters an a
# print(count) # counts how many a's are in the word

def count(s,letter):
    c=0
    for each in s:
        if each == letter:
            c+=1
    return c
print(count(team, 'a')) #should be 2

new_team= team.upper()
print(new_team)

#team.split() # [New,England Patriots]
#split,strip('a'),