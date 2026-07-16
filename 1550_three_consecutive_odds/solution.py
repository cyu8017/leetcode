# LeetCode 1550

class Solution:
    def threeConsecutiveOdds(self, arr):
        run = 0
        for value in arr:
            run = run + 1 if value & 1 else 0
            if run == 3:
                return True
        return False
