#Excercise03

#split,strip,replace

team= 'New England Patriots'
print(team.split('')) #['New','England','Patriots']
print(team.split('e')) #['N','w England Patriots']
print(team.strip('')) #New England Patriots
print(team.replace('England', 'New')) #New New Patriots , replaces England with New
print(team.replace('','~')) #New~England~Patriots
#othermethods
print(team.isalnum()) #False
print(team.isalpha()) #False bc spaces
print('team'.isalpha()) #true bc team is all alpha
print(team.isspace()) #False
print(team.upper()) #NEW ENGLAND PATRIOTS
print(team.lower()) #new england patriots

#Excercise04

#1.You walk into a store where each item is priced according to the letter in its name: 'a' costs $1, 'b' is $2, and so on. Write a program that prints a receipt for this wacky store:

#bananas $52
#rice $35
#paprika $72
#potato chips $78
#-----------------
#Total $237

a = ord('a') -96
b = ord('b') -96
c = ord('c') -96
n = ord('n') -96
s = ord('s') -96
r = ord('r') -96
i = ord('i') -96
e = ord('e') -96
p = ord('p') -96
k = ord('k') -96
o = ord('o') -96
t = ord('t') -96
h = ord('h') -96

bananas = b+ (a*3) + (n*2) + s
print(bananas)
rice = r + i + c + e
print(rice)
paprika = (p*2) +(a*2) + r +i +k
print(paprika)
potato_chips= (p*2) + (o*2) + (t*2) + a + c + h + i +s
print(potato_chips)

total= bananas +rice + paprika + potato_chips
print(total)

print('bananas ${:d}'.format(bananas))
print('rice ${:d}'.format(rice))
print('paprika ${:d}'.format(paprika))
print('potato chips ${:d}'.format(potato_chips))
print('---------------------')
print('Total ${:d}'.format(total))

#final print of receipt
print('bananas ${:d}'.format(bananas), 'rice ${:d}'.format(rice), 'paprika ${:d}'.format(paprika), 'potato chips ${:d}'.format(potato_chips), '------------------', 'Total ${:d}'.format(total), sep="\n")
#final print with decimals
print('bananas ${:.2f}'.format(bananas), 'rice ${:.2f}'.format(rice),'paprika ${:.2f}'.format(paprika), 'potato chips ${:.2f}'.format(potato_chips),'------------------', sep"\")
