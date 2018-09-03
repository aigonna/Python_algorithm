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
# temp = Node(93)
# print(temp.getData())

class UnorderList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)#create a new Node,and set insert element as Node data
        temp.setNext(self.head)#set new insert element quote as former list head node
        self.head = temp #set list head to the new node

    def size(self):
        current = self.head#initialize current to list head
        count = 0 #initialize node count as 0
        while current != None:
            count = count + 1
            current = current.getNext()#current move to next node
        return count

    def search(self, item):
        current = self.head  #initialize current to list head
        found = False
        while current != None and not found: #judge current is not None and found is False
            if current.getData() == item: #if current data is item
                found = True
            else:
                current = current.getNext()
        return found

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

mylist = UnorderList()
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
