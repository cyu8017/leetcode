# LeetCode 1518

class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        total = numBottles
        while numBottles >= numExchange:
            new, remainder = divmod(numBottles, numExchange)
            total += new
            numBottles = new + remainder
        return total
