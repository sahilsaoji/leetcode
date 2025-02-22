class Solution(object):
    def twoSum(self, nums, target):
        lastNum = len(nums)
        #last number in the list
        for i in range(lastNum-1):
        #we're iterating through the list 
            for j in range(i+1, lastNum):
                #So this is all the numbers past i and just seeing if   add to target
                if nums[i] + nums[j] == target:
                    return [i,j]
        return