fin = open("session09/words.txt")
line = repr(fin.readline())
word = line.strip()
# print(word)

counter = 0

# for line in fin:
#     word= line.strip()
#     counter += 1 
#     print(counter)

def read_long_words():
    """
    prints only the words with more than 20 characters
    """
    counter= 0

    for line in fin:
        word = line.strip()
        if len(word) > 20:
        # print(word)



def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter “e” in it.
    """
    # for letter in word:
    #     if letter == 'e':
    #         return False
    # return True 
    return not 'e' in word.lower() #same thing

print(has_no_e('Babson'))
print(has_no_e('College'))


def avoids(word, forbidden):
    """
    takes a word and a string of forbidden letters, and that returns True
    if the word doesn’t use any of the forbidden letters.
    """
    return not forbidden in word 


print(avoids('Babson', 'ab'))
print(avoids('College', 'ab'))


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    for letter in word:
        if letter not in available:
            return False
    return True




print(uses_only('Babson', 'aBbsonxyz'))
print(uses_only('college', 'aBbsonxyz'))


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for letter in reequired:
        if letter not in word:
            return False
    return True


print(uses_all('Babson', 'abs'))
print(uses_all('college', 'abs'))


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    last_letter = word [0]
    for c in word:
        if c < last_letter:
            return False
        last_letter = c
    return True


print(is_abecedarian('abs'))
print(is_abecedarian('college'))

#excercise02
#Rewrite abecedarian using recursion
def is_abecedarian_recursion(word):
    if len(word) == 1:
        return True
    elif ord(word [1]) < ord(word[0]):
        return False
    else:
        return is_abecedarian_recursion(word [1:])

print(is_abecedarian_recursion('abs'))
print(is_abecedarian_recursion('college'))

#Rewrite abecedarian using while loop

def is_abecedarian_while(word):
    iteration=0
    while iteration< len(word):
        previous = word[0]
        for c in word:
            if c < last_letter:
                return False
            last_letter = c
        return True

print(is_abecedarian_while('abs'))
print(is_abecedarian_while('college'))
