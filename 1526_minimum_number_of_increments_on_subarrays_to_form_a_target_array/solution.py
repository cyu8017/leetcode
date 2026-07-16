# LeetCode 1526

class Solution:
    def minNumberOperations(self, target):
        return target[0] + sum(max(0, target[i] - target[i - 1]) for i in range(1, len(target)))
