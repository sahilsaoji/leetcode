class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #Step 1: have to sort every pair in the intervals list based on the first value of the pair
        #Step 2: Iterate through the intervals list two at a time
            # Step 2a: if y1 >= x2 where the current interval is x1,y1 and the next interval is x2, y2 then we know the intervals intersect. There are three possible cases of interception.  
                #Case1: y1 > y2, then the new interval is x1,y1
                #Case2: y1 == y2, then the new interval is x1,y1
                #Case3: y1 < y2, then the new interval is x1,y2
                #Remove the current and next interval and add in the new merged interval which becomes the location of the new pointer and i+1 is the next one
            # Step 2b: else move to the next pair
        #Step 3: iterate through until we get to the second to last interval
        #Step 5: return
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            current = intervals[i]
            last = result[-1]

            if last[1] >= current[0]:
                last[1] = max(last[1], current[1])
            else:
                result.append(current)

        return result