import os
print(os.getcwd())

fout = open('session14/output.txt','a') # a creates a new text file and adds
line1 = "How many roads must a man walk down\n"
fout.write(line1)
line2 = "Before you call him a man?\n"
fout.write(line2)
fout.close() #you need to close it so it doesn't stay open 

print(os.path.abspath('session14/output.txt'))

print(os.path.exists('session14/output.txt')) #True
print(os.path.exists('session14/input.txt')) #False checks if it exists


import pickle
# t1 = [1,2,3]

# f = open('save.p', 'wb')
# s = pickle.dump(t1,f)
# f.close()


t2 = pickle.load(open('save.p', 'rb'))

print(t2)