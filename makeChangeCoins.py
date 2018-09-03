#coding = utf-8
def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

#print(recMC([1, 5, 10, 25], 15))#67,716,925

def recDC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1 #save numbers of min coins in knownResults
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change -i, knownResults)#recursive call recDc method
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins

#print(recDC([1, 5, 10, 25], 63, [0]*64))

def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(change + 1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        minCoins[cents] = coinCount
    return minCoins[change]

#print(dpMakeChange([1, 5, 10, 25], 63, [0]*64))

def dpMakechanges(coinValueList, change, minCoins, coinUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinUsed[cents] = newCoin
    return minCoins[change]
def printCoints(coinUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coinUsed = [0]*(amnt + 1)
    coinCount = [0]*(amnt + 1)

    print("Making change for", amnt, "requires: ")
    print(dpMakechanges(clist, amnt, coinCount, coinUsed), "coins")
    print("They are:")
    printCoints(coinUsed, amnt)
    print("The used list is as follows:")
    print(coinUsed)

if __name__ == "__main__":
    main()