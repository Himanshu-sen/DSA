class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ns = ''
        for i in s:
            if i.isalnum():
                ns+=i.lower()
        start = 0
        end = len(ns)-1
        while start<end:
            if ns[start]==ns[end]:
                start+=1
                end = end - 1
            else:
                return False
        return True
        