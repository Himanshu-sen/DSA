class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minbuy = prices[0]
        maxp = 0
        for sell in prices:
            maxp = max(maxp,sell - minbuy)
            minbuy = min(sell, minbuy)
        return maxp
        