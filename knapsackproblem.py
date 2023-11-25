# Libraries Included:
# Numpy, Scipy, Scikit, Pandas
# 
# Old Content below(Python 2):
# 
# # Libraries Included:
# # Numpy, Scipy, Scikit, Pandas
# """
# An automobile mechanic wants to buy a set of spare parts from a manufacturing unit.
# The cost of buying the ith spare part is cost[i], and the mechanic charges an amount of 2^i
# for replacing the th spare part with a new one. The manufacturing unit deals in a
# total of n items. The mechanic has a total of x amount of money, which the mechanic
# can spend on buying spare parts.
# 
# The goal is to maximize the total amount of money the mechanic
# can earn for a given amount x. As the answer can be rather large,
# report the answer as moneyEarned % (109+7), where % denotes
# modulo operator.
# 
# Ex 1:
# cost = [10, 20, 14, 40, 50]
# x = 70
# 
# Output: 20
# """
# 
# 
# 
"""
1. recursive structure (base case, other case)
2. recurrence relation (an aggregating function that lets you determine between branches)
3. memoizaztion (taking it to a more optimized complexity via a DP data structure)

def moneyHelper(cost, x, i)
# returns: the most money you can make, starting at index i, with cost cap x
# findMaximumMoneyEarned(cost, x) = moneyHelper(cost, x, 0)

"""


def moneyHelper(cost, x, i, memoization):
    if memoization is None:
        memoization = {}
    
    if (i, x) in memoization:
        return memoization[(i, x)]
    
    if i >= len(cost) or x <= 0:
        return 0
    
    skip = moneyHelper(cost, x, i+1, memoization)
    
    profit = 0
    
    if x >= cost[i]:
        profit = (2**i + moneyHelper(cost, x-cost[i], i+1, memoization))
                  
    memoization[(i,x)] = max(skip, profit)
    #print(memoization)
    
    return memoization[(i, x)]
        

def findMaximumMoneyEarned(cost,x):
    print(moneyHelper(cost, x, 0, None))
    
findMaximumMoneyEarned([10, 20, 14, 40, 50],70)
    
        
