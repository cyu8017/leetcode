# LeetCode 3992 - Rearrange String to Avoid Character Pair
# https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/


class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        arr = list(s)
        i = 0
        for j in range(len(arr)):
            if arr[j] == y:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        return "".join(arr)
