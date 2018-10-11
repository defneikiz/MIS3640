grades = dict()
#print(grades)
grades['Defne'] = 90
# print(grades)
grades ={'Defne': 90, 'Jack': 75, 'Angela':85}
# print(grades)

def histogram(string):
    d= dict()
    for letter in string:
        # if letter not in d: # if letter is not in the dictionary yet
        #     d[letter] = 1  # the value is one
        # else: #if the letter is already in the dictionary
        #     d[letter] += 1 #add one to the value of the letter
        d[letter] = d.get(letter,0) + 1 #default is zero for each letter but if that letter is available, then we add 1
    return d #lays out the whole dictionary


h= histogram ('Bookkeeper')
print(h)

def print_hist(h):
    for c in h:
        print(c,h[c])

h = histogram ('Massachusetts')
print_hist(h)
