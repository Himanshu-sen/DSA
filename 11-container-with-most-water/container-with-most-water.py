class Solution(object):
    def maxArea(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0 
        end = len(heights)-1
        res= 0
        while start < end:
            area = min(heights[start], heights[end])*(end - start)
            res = max(res, area)
            if heights[start]<=heights[end]:
                start+=1
            else:
                end-=1
        return res

        