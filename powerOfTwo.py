##def isPowerOfTwo(n):
##    if n==1:
##        return True
##    else:
##        while (n%2==0):
##            n = n/2
##            if n == 1:
##                return True
##        return False
##            
##print(isPowerOfTwo(24))


import math 

def isPowerOfTwo(n):
    return (math.ceil(math.log2(n)) == math.floor(math.log2(n)));
    

print(isPowerOfTwo(16))
