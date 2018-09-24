#Excercise1_1
result= 0


# for i in range (1,11):
#     print('current number to be added',i)
#     result= result + i 
#     print('new result after this iteration:',result)
# print('The final result:',result)

#Excercise1_2

for i in range(1,1001):
    print('current number to be added',i)
    result=result+i
    print('new result after this iteration:', result)
print('The final result:',result)

#excercise1_3 odd number
for i in range(1,11):
    if i % 2 == 0:
        print(i, 'is an even number')
    else:
        print(i,'is an odd number')

result= 0
#for sum of odd numbers
for i in range (1, 1001):
    if i % 2 == 1: #if we divide a number by 2, the remainder is 1, so its an odd number
        result=result + i

print('The sum of odd numbers is',result)

#for sum of even numbers
result=0
for i in range (1,1001):
    if i % 2==0:
        result= result + i
print('The sum of even numbers is', result)

#alternative way to add odd numbers
result=0
for i in range(1,1001,2): #we start from 1, and we keep adding 2 to the next number 1, 3, 5
    result=result+i

print('The sum of odd numbers is', results)

#factorial calculation with loop

result=1 #we are using multiplication if we set to 0, the result would be 0 always
for i in range(1,10):
    result= result * i 

print('The factorial of 10 is',result)

#while statement
#while something is true, execute it, until it is not true, skip
 
import time

def countdown(n):
    while n>0:
        print(n)
        time.sleep (1)
        n = n-1
    print('Blastoff!')

countdown(5)

while counter< 10:
    print(r"Here's Johnny!") #r writes as is, no need for \ before ' or "
    counter +=1 #same as counter= counter+1

#counting letters  can use function len() to tell number of letters

message = 'Pranjal'

for letter in message:
    print(letter)

#doesn't understand what letter actually is but can use i or anything else.

#excercise2

iteration=0
count=0
while iteration < 5:
    #the variable letter in the room stands for every character including spaces and commas
    for letter in "hello, world":
        count += 1 
    print("iteration"+ str(iteration)+ ";count is :" + str(count))
    iteration +=1

#learning brake

while True:
    line= input('>')
    if line == 'done':
        break
    print(line)

print('Done!')