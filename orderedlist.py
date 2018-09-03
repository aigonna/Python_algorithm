class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class Orderedlist:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head#initialize current to list head
        count = 0 #initialize node count as 0
        while current != None:
            count = count + 1
            current = current.getNext()#current move to next node
        return count

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:#if data save in current node > search element, set stop as True
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def remove(self, item):
        current = self.head #initialize current to list head
        previous = None #previous:previous always next to current a node in traversal all list
        found = False
        while not found:
            if current.getData() == item:#if element in  node unit is pre-remove element, found turn to True
                found = True
            else:#(inch-worming)
                previous = current # previous move to current node,current move to next node
                current = current.getNext()
        if previous == None:
            self.head = current.getNext() #list head move to current next node
        else:
            previous.setNext(current.getNext())#previous node set to current next node

mylist = Orderedlist()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
print(mylist.search(17))
print(mylist.remove(17))
print(mylist.remove(31))
print(mylist.search(31))
