#list operation
myList = [1024, 3, True, 6.3]
myList.append(False)
print(myList)
myList.insert(2, 4.5)
print(myList)
print(myList.pop())
print(myList)
print(myList.pop(1))
print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)
print(myList.count(6.5))
print(myList.count(1024))
print(myList.index(4.5))
print(myList)
del myList[1]
print(myList)

#string
myName = 'David'
print(myName[3])
print(myName*2)
print(len(myName))
print(myName.upper())
print(myName.center(12))
print(myName.find('v'))
print(myName.split('v'))
myList1 = [1, 3, True, 6.5]
myList1[0] = 2**10
print(myList1)
myList[0] = 'X'
print(myList[0])

#set
mySet = {3.6, "cat", 4.5, False}
print(mySet)
print(len(mySet))
print(False in mySet)
Set1 = {'dog'}
print(mySet.union(Set1))
print(mySet.intersection(Set1))
print(mySet.difference(Set1))
print(mySet.issubset(Set1))
mySet.add("house")
print(mySet)
mySet.clear()
print(mySet)

#dictionary
capitals = {'lowa':'DesMoines', 'Wisconsin':'Madision'}
for k in capitals:
    print(capitals[k], "is the captial of", k)


phoneext = {'David':1410, 'Brad':1137}
print(phoneext)
print(phoneext.keys())
print(list(phoneext.keys()))
print(phoneext.values())
print(phoneext.items())
print(phoneext.get("keny"))

#letter print
wordlist = ['cat', 'dog', 'rabbit']
letterlist = []
for aword in wordlist:
    for aletter in aword:
        if aletter not in letterlist:
            letterlist.append(aletter)
print(list(letterlist))

#Newdown method
def squareroot(n):
    root = n/2
    for k in range(20):
        root = (1/2)*(root + (n/root))
    return root
print(squareroot(9))
print(squareroot(1890))

