class AnagramDetection:

    #first:listed two string, sorted two string, compare every string in order
    def anagramSolution1(self, s1, s2):
        alist1 = list(s1)
        alist2 = list(s2)

        alist1.sort()
        alist2.sort()

        pos = 0
        matches = True

        while pos < len(s1) and matches:
            if alist1[pos] == alist2[pos]:
                pos = pos+1
            else:
                matches = False

        return matches

    def anagramSolution2(self, s1, s2):
        c1 = [0] * 26
        c2 = [0] * 26

        for i in range(len(s1)):
            pos = ord(s1[i]) - ord('a')
            c1[pos] = c1[pos] + 1

        for i in range(len(s2)):
            pos = ord(s2[i]) - ord('a')
            c2[pos] = c2[pos] + 1
        j = 0
        stillOK = True
        while j < 26 and stillOK:
            if c1[j] == c2[j]:
                j = j + 1
            else:
                stillOK = False
        return stillOK

    def anagramSolution3(self, s1, s2):
        alist1 = list(s1)
        alist2 = list(s2)

        aset1 = set(alist1)
        aset2 = set(alist2)

        if aset1 != aset2:
            return False
        else:
            for ch in aset1:
                if alist1.count(ch) != alist2.count(ch):
                    return False

            return True

s1, s2, s3 = 'abcde', 'afcde', 'acbde'
test = AnagramDetection()
print(test.anagramSolution1(s1, s3))
print(test.anagramSolution1(s1, s2))
print(test.anagramSolution2(s1, s3))
print(test.anagramSolution2(s1, s2))
print(test.anagramSolution3(s1, s3))
print(test.anagramSolution3(s1, s2))

