# LeetCode 1898 - Maximum Number of Removable Characters
# https://leetcode.com/problems/maximum-number-of-removable-characters/

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: list[int]) -> int:
        def still_subsequence(k: int) -> bool:
            removed = set(removable[:k])
            index = 0
            for position, char in enumerate(s):
                if position in removed:
                    continue
                if index < len(p) and char == p[index]:
                    index += 1
            return index == len(p)

        lo, hi = 0, len(removable)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if still_subsequence(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
