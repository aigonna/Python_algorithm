class Stack():
    #stack initize
    def __init__(self):
        self.items = []

    #stack is empty or not
    def isEmpty(self):
        return self.items == []

    #push an element to stack top
    def push(self, item):
        self.items.append(item)

    #put stack bottom element out
    def pop(self):
        return self.items.pop()

    #return stack top element2
    def peek(self):
        return self.items[len(self.items)-1]
    #return stack size
    def size(self):
        return len(self.items)

# s = Stack()
# print(s.isEmpty())
# s.push(4)
# print(s.peek())
# s.push('dog')
# print(s.peek())
# print(s.isEmpty())
# s.push(True)
# print(s.peek())
# s.push('True')
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())



def revstring(mystr):
    s = Stack()
    outputStr = ''
    for c in mystr:
        s.push(c)
    while not s.isEmpty():
        outputStr += s.pop()
    return outputStr

# print(revstring('apple'))
# print(revstring('x'))
# print(revstring('1234567890'))

def matches(open, close):
    opens = '([{'
    closers = '}]}'
    return opens.index(open) == closers.index(close)

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            top = s.pop()
            if not matches(top, symbol):
                balanced = False
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


#print(parChecker('({[]})'))

def Dec2Bin(decNumber):

    s = Stack()
    while decNumber > 0:
        temp = decNumber % 2
        s.push(temp)
        decNumber = decNumber // 2
    binString = ''
    while not s.isEmpty():
        binString += str(s.pop())
    return binString

# print(Dec2Bin(42))

def baseConverter(decNumber, base):
    digits = '012345GH'
    s = Stack()
    while decNumber > 0:
        temp = decNumber % base
        s.push(temp)
        decNumber = decNumber//base

    newString = ''
    while not s.isEmpty():
        newString = newString + digits[s.pop()]
    return newString

# print(baseConverter(8, 2))
# print(baseConverter(16, 4))
