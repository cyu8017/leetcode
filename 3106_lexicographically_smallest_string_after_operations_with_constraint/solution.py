# LeetCode 3106 - Lexicographically Smallest String After Operations With Constraint
# https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/


class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        arr = list(s)
        for i in range(len(arr)):
            c1 = ord(arr[i])
            for c2 in range(97, c1):
                d = min(c1 - c2, 26 - (c1 - c2))
                if d <= k:
                    arr[i] = chr(c2)
                    k -= d
                    break
        return "".join(arr)
