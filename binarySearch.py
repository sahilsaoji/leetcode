class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # for i in range(0,len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1
        
        #how to go through binary search 
        #This was just iterating through each value 
        #binary search would be creating a left and right value, and while your left is less than your right you first iterate on your middle, then check if middle = target and if it does you return the middle, else target<middle then right right is the middle, and vice versa 
        left = 0
        right = len(nums)-1
        while(left<=right):
          mid = (left+right)/2
          if nums[mid] == target:
            return mid
          elif nums[mid]>target:
            right = mid-1
          else:
            left = mid+1
        
        return -1