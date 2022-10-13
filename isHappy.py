def isHappy(self, n):   
    def nextNumber(n):
        sumofNums = 0
        while (n>0):
            tempNum = n%10
            n = n/10
            tempNum = tempNum*tempNum
            sumofNums = sumofNums + tempNum
        return sumofNums

    hashMap = set()
    while n!= 1 and n not in hashMap:
        hashMap.add(n)
        n = nextNumber(n)

    return n==1

