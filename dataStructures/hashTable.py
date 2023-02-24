class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def getHash(self, key):
        hash = 0

        for char in key:
            hash += ord(char)

        return hash % self.MAX
    
    def __setitem__(self, key, value):
        h = self.getHash(key)
        found = False

        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True

        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.getHash(key)

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.getHash(key)

        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                print('del', index)
                
                del self.arr[h][index]

hashTable = HashTable()

# getHash()
print(hashTable.getHash('march 6'))
print(hashTable.getHash('march 17'))

# __setitem__
hashTable['march 6'] = 120
hashTable['march 7'] = 67
hashTable['march 8'] = 4
hashTable['march 9'] = 459
hashTable['march 17'] = 63457

# __getitem__
print(hashTable.arr)

# __delitem__
del hashTable['march 17']
print(hashTable.arr)
