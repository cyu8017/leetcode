# LeetCode 0898 - Bitwise ORs of Subarrays
# https://leetcode.com/problems/bitwise-ors-of-subarrays/

class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        ans: set[int] = set()
        cur: set[int] = set()
        for x in arr:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)
