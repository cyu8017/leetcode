# LeetCode 1540

class Solution:
    def canConvertString(self, s, t, k):
        if len(s) != len(t):
            return False
        used = [0] * 26
        for a, b in zip(s, t):
            shift = (ord(b) - ord(a)) % 26
            if shift:
                used[shift] += 1
                if shift + 26 * (used[shift] - 1) > k:
                    return False
        return True
