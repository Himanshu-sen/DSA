class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers)-1
        while start < end:
            nsum = numbers[start]+numbers[end]
            if nsum < target:
                start+=1
                
            elif nsum > target:
                # start+=1
                end -= 1
            else:
                return [start+1, end+1]
                # end-=1
        return []
        