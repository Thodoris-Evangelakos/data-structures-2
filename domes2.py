#https://www.youtube.com/watch?v=YlgPi75hIBc
#https://www.myabandonware.com/game/m1-tank-platoon-ii-49u

N = 10**6
n = 10**2
insertComparisons = 0
deleteComparisons = 0
milKeys = "millionKeys.bin"
hunKeys = "hundredKeys.bin"

class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None
        
    def insCompN(self):
        global insertComparisons
        insertComparisons += 1
    
    def insert(self, data):
        if self.value == data:
            self.insCompN()
            return False
        elif data < self.value:
            self.insCompN()
            if self.leftChild:
                self.insCompN()
                return self.leftChild.insert(data)
            else:
                self.insCompN()
                self.leftChild = Node(data)
                return True
        else:
            self.insCompN()
            if self.rightChild:
                self.insCompN()
                return self.rightChild.insert(data)
            else:
                self.insCompN()
                self.rightChild = Node(data)
                return True
    
    def find(self, data): #FINNA CHANGE THIS DAS RITE
        if(data == self.value):
            return True
        elif(data < self.value):
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False
        
class Tree:
    def __init__(self):
        self.root = None
        
    def insComp(self):
        global insertComparisons
        insertComparisons += 1
    
    def delComp(self):
        global deleteComparisons
        deleteComparisons += 1
        
    def insert(self, data):
        if self.root:
            self.insComp()
            return self.root.insert(data)
        else:
            self.insComp()
            self.root = Node(data)
            return True
    
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    
    def search(self, data): #find the node to delete
        leParent = None
        leNode = self.root
        while leNode and leNode.value != data:
            self.delComp()
            leParent = leNode
            if data < leNode.value:
                self.delComp()
                leNode = leNode.leftChild
            elif data > leNode.value:
                self.delComp()
                leNode = leNode.rightChild
        leNodeAndleParent = [leNode, leParent]
        return leNodeAndleParent
    
    def remove(self, data):
        #empty tree
        if self.root is None:
            self.delComp()
            return False
        
        #data is in root node
        elif self.root.value == data:
            self.delComp()
            if self.root.leftChild is None and self.root.rightChild is None:
                self.delComp()
                self.root = None
            elif self.root.leftChild and self.root.rightChild is None:
                self.delComp()
                self.root = self.root.leftChild
            elif self.root.leftChild is None and self.root.rightChild:
                self.delComp()
                self.root = self.root.rightChild
            elif self.root.leftChild and self.root.rightChild:
                self.delComp()
                delNodeParent = self.root
                delNode = self.root.rightChild
                self.delComp()
                while delNode.leftChild:
                    self.delComp()
                    delNodeParent = delNode
                    delNode = delNode.leftChild
                
                self.root.value = delNode.value
                if delNode.rightChild:
                    self.delComp()
                    if delNodeParent.value > delNode.rightChild:
                        self.delComp()
                        delNodeParent.leftChild = delNode.rightChild
                elif delNodeParent.value < delNode.value:
                    self.delComp()
                    delNodeParent.rightChild = delNode.rightChild
                else:
                    self.delComp()
                    if delNode.value < delNodeParent.value:
                        self.delComp()
                        delNodeParent.leftChild = None
                    else:
                        self.delComp()
                        delNodeParent.rightChild = None
    
        nodeAndParent = self.search(data)
        node = nodeAndParent[0]
        parent = nodeAndParent[1]
        
        #case 1: data is not found
        if node is None or node.value != data:
            self.delComp()
            return False
            
        #case 2: remove-node has no children
        elif node.leftChild is None and node.rightChild is None:
            self.delComp()
            if data < parent.value:
                self.delComp()
                parent.leftChild = None
            else:
                self.delComp()
                parent.rightChild = None
            return True
        
        #case 3: remove-node has left child only
        elif node.leftChild and node.rightChild is None:
            self.delComp()
            if data < parent.value:
                self.delComp()
                parent.leftChild = node.leftChild
            else:
                self.delComp()
                parent.rightChild = node.leftChild
            return True
                
        #case 4: remove-node has right child only
        
        elif node.leftChild is None and node.rightChild:
            self.delComp()
            if data < parent.value:
                self.delComp()
                parent.leftChild = node.rightChild
            else:
                self.delComp()
                parent.rightChild = node.rightChild
            return True
        
        #case 5: remove-node has both left and right child
        else:
            self.delComp()
            delNodeParent = node
            delNode = node.rightChild
            self.delComp()
            while delNode.leftChild:
                self.delComp()
                delNodeParent = delNode
                delNode = delNode.leftChild
            
            node.value = delNode.value
            if delNode.rightChild:
                self.delComp()
                if delNodeParent.value > delNode.value:
                    self.delComp()
                    delNodeParent.leftChild = delNode.rightChild
                elif delNodeParent.value < delNode.value:
                    self.delComp()
                    delNodeParent.rightChild = delNode.rightChild
            else:
                self.delComp()
                if delNode.value < delNodeParent.value:
                    self.delComp()
                    delNodeParent.leftChild = None
                else:
                    self.delComp()
                    delNodeParent.rightChild = None

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
    bst = Tree()
    #print(os.listdir())
    start = timer(0)
    with open(milKeys, 'rb') as file:
        for i in range (0,N):
            bst.insert(readInt(file, i))
    print("total time for 10^6 insertions: ", timer(1)-start)
    print("avg number of comparisons per insertion: ", insertComparisons/N)

    start = timer(0)
    with open(hunKeys, 'rb') as file:
        for i in range(0,n):
            bst.remove(readInt(file,i))
    print("total time for 100 removals: ", timer(1)-start)
    print("avg number of comparisons per removal: ", deleteComparisons/n)

    return 0

if __name__ == '__main__':
    #imports
    import os
    import random
    import numpy as np
    import timeit
    import time
    
    main()
