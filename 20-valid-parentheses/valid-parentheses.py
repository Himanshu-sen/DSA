class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        checker = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in checker:
                x = stack.pop() if stack else "#"
                if checker[i] != x:
                    return False
            else:
                stack.append(i)
        return False if stack else True      