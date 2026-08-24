# LeetCode 3794 - Reverse String Prefix
# https://leetcode.com/problems/reverse-string-prefix/

class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        arr = list(s)
        i, j = 0, k - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return "".join(arr)
