class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m-1
        while start<=end:
            mid = (start+end)//2
            if matrix[mid][0]<target:
                start = mid+1
            elif matrix[mid][0]>target:
                end = mid -1
            else:
                break
        row = (start+ end)//2
        start = 0
        end = n-1
        while start<=end:
            mid = (start+end)//2
            if matrix[row][mid]<target:
                start = mid+1
            elif matrix[row][mid]>target:
                end = mid -1
            else:
                return True
        return False
        