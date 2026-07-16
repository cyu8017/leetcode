# LeetCode 1529

class Solution:
    def minFlips(self, target):
        return sum(a != b for a, b in zip("0" + target, target))
