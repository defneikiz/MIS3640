def move(n, source, bridge, destination):
    if n >=1:
        move(n-1,source,bridge,destination)
        movedisk(source, destination)
        move(n-1, bridge, destination, source)

def movedisk(source,destination):
    print('moving disk from {} to {}'. format(source,destination))



print (move(3,"A","B","C"))