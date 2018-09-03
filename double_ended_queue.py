class Deque:
     def __init__(self):
         self.items = []

     def isEmpyty(self):
         return self.items == []

     #insert an element in deque front, parameter:pre-insert element
     def addFront(self, item):
         self.items.append(item)

     #insert an element in deque rear, parameter:pre-insert element
     def addRear(self, item):
         self.items.insert(0, item)

     #remove an element in deque front, return:element
     def removeFront(self):
         return self.items.pop()

     #remove an element in deque rear, return:element
     def removeRear(self):
         return self.items.pop(0)

     def size(self):
         return len(self.items)

# deque = Deque()
# print(deque.isEmpyty())
# deque.addRear(4)
# deque.addRear('dog')
# deque.addFront('cat')
# deque.addFront(True)
# print(deque.size())
# print(deque.isEmpyty())
# deque.addRear(8.4)
# print(deque.removeRear())
# print(deque.removeFront())

def palchecker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)
    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual

print(palchecker('ssfjksfjsfj'))
print(palchecker('radar'))