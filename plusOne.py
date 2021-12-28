class Solution(object):
    def plusOne(self, digits):
        strings = [str(digit) for digit in digits]
        a_string = "".join(strings)
        an_integer = int(a_string)
        an_integer = an_integer + 1
        
        digit_string = str(an_integer)


        digit_map = map(int, digit_string)


        digit_list = list(digit_map)
        return digit_list
        
        """
        for i in range(len(digits)-1):
            if digits[i] == 9:
                if len(digits) == 1:
                    digits.remove(9)
                    digits.append(0)
                    digits.append(1)
                    print(digits)
                    return digits
                else:
                    digits[i] = 0
                    digits[i-1] = digits[i-1] + 1
                    return digits 
        digits[len(digits)-1] = digits[len(digits)-1] + 1
        return digits
        """
        
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
