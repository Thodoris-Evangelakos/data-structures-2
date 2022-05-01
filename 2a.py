N = 10**6
n = 10**2
insertComparisons = 0
deleteComparisons = 0
milKeys = "millionKeys.bin"
hunKeys = "hundredKeys.bin"

def insComp():
        global insertComparisons
        insertComparisons += 1

def delComp():
        global deleteComparisons
        deleteComparisons += 1

def comp(command):
    if command == 0: #input 0 to increment insertComparisons by 1
        insComp()
    else: #input anything else to increment deleteComparisons by 1
        delComp() 

def resetComparisons(command):
    global insertComparisons
    global deleteComparisons
    if command == 0:
        insertComparisons = 0
    else:
        deleteComparisons = 0

#heap operations I definitely made myself

def heappush(heap, item, comparison):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1, comparison)

def heapify(x, comparison):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    n = len(x)
    # Transform bottom-up.  The largest index there's any point to looking at
    # is the largest with a child index in-range, so must have 2*i + 1 < n,
    # or i < (n-1)/2.  If n is even = 2*j, this is (2*j-1)/2 = j-1/2 so
    # j-1 is the largest, which is n//2 - 1.  If n is odd = 2*j+1, this is
    # (2*j+1-1)/2 = j so j-1 is the largest, and that's again n//2-1.
    for i in reversed(range(n//2)):
        comp(comparison)
        _siftup(x, i, comparison)

def _siftdown(heap, startpos, pos, comparison):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        comp(comparison)
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        comp(comparison)
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem

def _siftup(heap, pos, comparison):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        comp(comparison)
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        comp(comparison)
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos, comparison)

class Heap:
    def __innit__(self):
        self.heap = []

    def clear(self):
        self.heap = []

    def compH(self, command):
        if command == 0: #input 0 to increment insertComparisons by 1
            insComp()
        else: #input anything else to increment deleteComparisons by 1
            delComp()
    
    def insertOneAtATime(self):
        with open(milKeys, 'rb') as file:
            for i in range (0,N):
                self.compH(0)
                heappush(self.heap, readInt(file, i), 0)
    
    def insertAllAtOnce(self):
        temp = []
        with open(milKeys, 'rb') as file:
            for i in range (N):
                self.compH(0)
                temp.append(readInt(file, i))
            self.heap = temp
            heapify(self.heap,0)

    def getMaxKey(self):
        max = 0
        for i in range(0, N):
            if self.heap[i] > data:
                max = self.heap[i]
        return max
    
    def getKeyPos(self, key):
        posList = []
        for i in range (0,N):
            if self.heap[i] == key:
                posList.append(i)
        return posList

    def getPosOfMaxKeys(self):
        max = self.getMaxKey()
        posList = self.getKeyPos(max)
        return posList

    def removeKey(self, key):
        posList = self.getKeyPos(key)
        for i in range (0, len(posList)):
            self.heap[i] = self.heap[-1]
            self.heap.pop()
            heapify(heap)
    
    def removeMax(self):
        posList = self.getPosOfMaxKeys()
        for i in range (0, len(posList)):
            self.heap[i] = self.heap[-1]
            self.heap.pop()
            heapify(self.heap)        


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
    myHeap = Heap()
    start = timer(0)
    myHeap.insertAllAtOnce()
    print("total time for 10^6 insertions, all at once: ", timer(1)-start)
    print("avg comparisons per insertion, all at once:", insertComparisons/N)
    resetComparisons(0)
    myHeap.clear()
    myHeap.insertOneAtATime()
    print("total time for 10^6 insertions, one at a time: ", timer(1)-start)
    print("avg comparisons per insertion, one at a time:", insertComparisons/N)
    return 0

if __name__ == '__main__':
    #imports
    import numpy as np
    import timeit
    import time
    
    main()