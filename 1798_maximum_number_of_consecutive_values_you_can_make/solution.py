class Solution:
    def getMaximumConsecutive(self, coins):
        coins.sort()
        reach = 0
        for coin in coins:
            if coin > reach + 1:
                break
            reach += coin
        return reach + 1
