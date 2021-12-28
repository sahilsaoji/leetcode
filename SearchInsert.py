class Solution(object):
    def searchInsert(self, nums, target):
        
        if len(nums) == 0 : # Empty List
            return 0
        elif len(nums) == 1:
            return 0 if nums[0]>=target else 1 # Empty List
        
        # Deal with the first element
        if nums[0]>=target:
            return 0
        
        # Go through every element
        for idx in range(1,len(nums)):
            # If previous element is less than target, continue
            if nums[idx-1]>target:
                continue
            else:
            # Otherwise, we need to check and return corresponding index
                if nums[idx-1] == target:
                    return idx -1
                
                elif nums[idx] >= target:
                    return idx
        # If above conditions don't exist, that means target is bigger than those values
        return len(nums)

