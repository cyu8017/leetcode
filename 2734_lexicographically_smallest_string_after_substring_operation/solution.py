# LeetCode 2734 - Lexicographically Smallest String After Substring Operation
# https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/


class Solution:
    def smallestString(self, s: str) -> str:
        arr = list(s)
        n = len(arr)
        i = 0
        while i < n and arr[i] == "a":
            i += 1
        if i == n:
            arr[n - 1] = "z"
            return "".join(arr)
        while i < n and arr[i] != "a":
            arr[i] = chr(ord(arr[i]) - 1)
            i += 1
        return "".join(arr)
