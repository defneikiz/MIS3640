# print('a'.islower()) #True
# print('babson'.islower()) #True

def is_reverse(word1,word2):
    if len(word1) !=len(word2) #if the lenghts of the word are not the same we don't even bother to check if its reverse of each other
        return False
#DEBUGGING
#Debugging: When you create red dot left of numbers, it will make the code stop from being executed. 
#Use DEBUG CONSOLE to test out values. To test out what happens inside a function.
    i= 0
    j= len(word2)-1
    
    while j>0:
        print(i,j)
        if word1[i] !=word2[j]:
            return False
        i = i + 1
        j = j - 1
    return  Truee

# print(is_reverse('pots','stop'))

def in_both(word1,word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both('babson','college') #o