# LeetCode 0541 - Reverse String II
# https://leetcode.com/problems/reverse-string-ii/

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        for start in range(0, len(chars), 2 * k):
            end = min(start + k, len(chars)) - 1
            left, right = start, end
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        return "".join(chars)
