class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.replace(' ','')
        for i in string.punctuation:
            s = s.replace(i,'')
        s = s.lower()
        return s == s[::-1]
        