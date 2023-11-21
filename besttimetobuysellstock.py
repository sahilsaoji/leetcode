class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        #basically you have the first value of the list as the start price - if the next one is the right value of the list 

        left = 0 #buy stock
        right = 1 #sell stock 
        maxprofit = 0
        while right < len(prices):
            currentprofit = prices[right]-prices[left]
            if prices[left] > prices[right]:
                left = right 
            else:
                if currentprofit > maxprofit:
                    maxprofit = currentprofit
                else:
                    maxprofit = maxprofit
            right+=1
        return maxprofit 
            

#Given an array prices where prices[i] is the price of a stock at the ith day 
#find the lowest and highest in the string and see if they are consecutive and then subtract those two numbers 
# most efficient to go from both sides and start from the start and see which is the lowest possible value, while 
#But there is a problem with the fact that you aren't able to go through