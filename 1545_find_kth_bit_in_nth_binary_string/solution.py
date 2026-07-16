# LeetCode 1545

class Solution:
    def findKthBit(self, n, k):
        invert = False
        length = (1 << n) - 1
        while k != 1:
            middle = length // 2 + 1
            if k == middle:
                return "0" if invert else "1"
            if k > middle:
                k = length - k + 1
                invert = not invert
            length //= 2
        return "1" if invert else "0"
