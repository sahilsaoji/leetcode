class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))  # Convert number to list of characters
        last_occurrence = {int(digit): i for i, digit in enumerate(num_list)}  # Store last index of each digit
        
        # Traverse each digit
        for i, digit in enumerate(num_list):
            for d in range(9, int(digit), -1):  # Look for a larger digit (9 down to digit+1)
                if d in last_occurrence and last_occurrence[d] > i:
                    # Swap the digits
                    num_list[i], num_list[last_occurrence[d]] = num_list[last_occurrence[d]], num_list[i]
                    return int("".join(num_list))  # Convert list back to integer and return
        
        return num  # No swap needed
