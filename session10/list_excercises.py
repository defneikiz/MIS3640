
# def nested_sum(t):
#     """Computes the total of all numbers in a list of lists.

#     t: list of list of numbers

#     returns: number

#     Expected output:
#     >>> t = [[1, 2], [3], [4, 5, 6]]
#     >>> nested_sum(t)
#     21
#     """
#     # sum= 0
#     # for nested in t:
#     #     total += sum(nested)
#     # return total

# # print(nested_sum())

# def cumsum(t):
#     """Computes the cumulative sum of the numbers in t.

#     t: list of numbers

#     returns: list of numbers

#     Expected output:
#     >>> t = [1, 2, 3]
#     >>> cumsum(t)
#     [1, 3, 6]
#     """

#     total= 0
#     res= []
#     for x in t: #try not to change the list itself
#         total += x
#         res.append(total) # add (append) element to an argument
#     return res

# print(cumsum(t))

# def middle(t):
#     """Returns all but the first and last elements of t.

#     t: list

#     returns: new list

#     Expected output:
#     >>> t = [1, 2, 3, 4]
#     >>> middle(t)
#     [2, 3]
#     """
#     return t[1:-1] 
# t=[1,2,3,4,5,6,7]
# print(middle(t))
# print(t)
# # check professors notes for info on where memory is stored
# def chop(t):
#     """Removes the first and last elements of t.

#     t: list

#     returns: None

#     Expected output:
#     >>> t = [1, 2, 3, 4]
#     >>> chop(t)
#     >>> t
#     [2, 3]
#     """
#     # del t[0] #deletes,the first item
#     # del t[1]



# def is_sorted(t):
#     """Checks whether a list is sorted.

#     t: list

#     returns: boolean

#     Expected output:
#     >>> is_sorted([1, 2, 2])
#     True
#     >>> is_sorted(['b', 'a'])
#     False
#     """ #docstring
#     # previous = t[0]
#     # for c in t:
#     #     if c< previous:
#     #         return False
#     #         previous = c
#     # return True
#     #we expect to see true or false, sorted or not sorted
#     return t == t.sort() #doesn't change t into something else, just reorganize internally
#     print ( is_sorted(['a','b','b','c']))
#     print ( is_sorted(['a','b','c','b']))


# def is_anagram(word1, word2):
#     """Checks whether two words are anagrams

#     Two words are anagrams if you can rearrange the letters from one to 
#     spell the other.

#     word1: string or list
#     word2: string or list

#     returns: boolean

#     Expected output:
#     >>> is_anagram('stop', 'pots')
#     True
#     >>> is_anagram('different', 'letters')
#     False
#     >>> is_anagram([1, 2, 2], [2, 1, 2])
#     Ture
#     """
#     return sorted(word1) == sorted(word2)
# #when you rearrange (sort) they have to be the same to be reverses (anagrams) of each other
# print( is_anagram('stop', 'pots')) #true
# print( is_anagram([1,2,2],[2,1,2])) #true

# def has_duplicates(s):
#     """Returns True if any element appears more than once in a sequence.

#     s: string or list

#     returns: bool

#     output:
#     >>> print(has_duplicates('cba'))
#     False
#     >>> print(has_duplicates('abba'))
#     True
#     """
#     for x in s:
#         if  s.count(x)>1:
#             return True
#     return False #outdented so it can give false

# print(has_duplicates('cba'))
# print(has_duplicates('abba'))

# def has_adjacent_duplicates(s):
#     """Returns True if there are two same adjacent elements.

#     s: string or list

#     returns: bool

#     output:
#     >>> print(has_adjacent_duplicates('cba'))
#     False
#     >>> print(has_adjacent_duplicates('abca'))
#     False
#     >>> print(has_adjacent_duplicates('abbc'))
#     True
#     """
#     for i in range(len(s)-1) : #because you start from 0, and some dont have the 4th letter (bc we start drom 0)
#         if s[i] == s[i+1]: # so it moves to the next letter
#             return True
#     return False


# def main():
#     t = [[1, 2], [3], [4, 5, 6]]
#     # print(nested_sum(t))

#     # t = [1, 2, 3]
#     # print(cumsum(t))

#     # t = [1, 2, 3, 4]
#     # print(middle(t))
#     # chop(t)
#     # print(t)

#     # print(is_sorted([1, 2, 2]))
#     # print(is_sorted(['b', 'a']))

#     # print(is_anagram('stop', 'pots'))
#     # print(is_anagram('different', 'letters'))
#     # print(is_anagram([1, 2, 2], [2, 1, 2]))

#     # print(has_duplicates('cba'))
#     # print(has_duplicates('abba'))


# if __name__ == '__main__':
#     main()