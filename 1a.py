N = 10**6

class Node:
    def __innit__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if  data == self.value:
            return False
        elif data < self.value:
            if self.leftChild is not None:
                return "FIXME"

class Tree:
    def __innit__(self):
        self.root = None  

def timer(command): #input 0 to start timer, input anything else (1) to end it and return elapsed time
    if command == 0:
        start = timeit.default_timer()
        return start
    else:
        end = timeit.default_timer()
        return end

def readBytes(file, position): #reads 4 bytes
    file.seek(position)
    byte_array = bytearray(file.read(4))
    return byte_array

def toIntArray(bytes):
    result = [0]
    result[0] = int.from_bytes(bytes[0:4], 'big')
    return result[0]
    
def readInt(file, position):
    #pass a simple position to this method
    intFromFile = toIntArray(readBytes(file, position*4)) #position 0 reads at 0, position 1 reads at 4 and so on (TAKEN CARE OF HERE XXX)
    return intFromFile 

def main():
    bst = [[None for x in range(3)] for y in range(N)]
    print("...Done!")
    return 0

if __name__ == '__main__':
    #imports
    import random
    import numpy as np
    import timeit
    import time
    
    main()