class Solution(object):
    def findEvenNumbers(self, digits):
        numbers = []
        number = ""
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i!=j and j!=k and i!=k:
                        number = str(digits[i]) + str(digits[j]) + str(digits[k])
                        number = int(number)
                        if number >= 100 and number%2==0:
                            if number not in numbers:
                                numbers.append(number)
        numbers.sort()
        return(numbers)

        #The list of lists - that contains all different barcodes
        #allBarcodes = []
        #Create 10 times the amount of lists wanted by the user
        #have to add 1 because start at 1
        #helps take out some of the lists that are unneeded
        #for i in range(1, (AmountOfBarcodes*10)+1):
        #    barcode_i = []
        #    j = lengthOfBarCode
        #    while j>0:
        #        barcode_i.append(random.choice(digits))
        #        j-=1
        #    allBarcodes.append(barcode_i)
        #return allBarcodes
            
        
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
