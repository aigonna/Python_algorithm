#coding = utf-8
class HashTable:
    def __init__(self):
        self.size = 11 #tablesize
        self.slots = [None]*self.size #initialize slots
        self.data = [None]*self.size #initialize data

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots)) #get hashvalue

        if self.slots[hashvalue] == None:#if slot of table is none, replace key to table slot and data to table data
            self.slots[hashvalue] = key
            self.data[hashvalue] = data

        else:
            if self.slots[hashvalue] == key: #if slot of table is key, replace data to table data
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots)) #get next slot value
                while self.slots[nextslot] != None and self.slots[nextslot] != key: #while next slot is not None, next slot move to next None slot
                    nextslot = self.rehash(nextslot, len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def get(self, key):
        #get HashTable data by key
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def hashfunction(self, key, size):
        return key % size #return remiander as slot

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size #(oldhash move 1 step) % tablesize

HashTable = HashTable()
HashTable[54] = 'cat'
HashTable[26] = 'dog'
HashTable[93] = 'lion'
HashTable[17] = 'tiger'
HashTable[77] = 'bird'
HashTable[31] = 'cow'
HashTable[44] = 'goat'
HashTable[55] = 'pig'
HashTable[20] = 'chicken'
print(HashTable.slots)
print(HashTable.data)
print(HashTable[20])
HashTable[20] = 'duck'
print(HashTable[20])