# LeetCode 1056 - Confusing Number
# https://leetcode.com/problems/confusing-number/

class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotate = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        s = str(n)
        rotated = []
        for ch in reversed(s):
            if ch not in rotate:
                return False
            rotated.append(rotate[ch])
        return "".join(rotated) != s
