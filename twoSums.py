class Solution(object):
    def twoSum(self, nums, target):
        subtractor = 0
        for startIterator,i in enumerate(nums):
            subtractor = target - i
            for endIterator,j in enumerate(nums):
                if j == subtractor and startIterator != endIterator:
                    return [startIterator,endIterator]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
