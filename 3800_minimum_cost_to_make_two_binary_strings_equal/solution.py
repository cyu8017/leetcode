# LeetCode 3800 - Minimum Cost to Make Two Binary Strings Equal
# https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/

class Solution:
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        diff = [0, 0]
        n = len(s)
        for i in range(n):
            if s[i] != t[i]:
                diff[ord(s[i]) - 48] += 1
        ans = (diff[0] + diff[1]) * flipCost
        mx = max(diff[0], diff[1])
        mn = min(diff[0], diff[1])
        ans = min(ans, mn * swapCost + (mx - mn) * flipCost)
        avg = (mx + mn) // 2
        ans = min(ans, (avg - mn) * crossCost + avg * swapCost + (mx + mn - avg * 2) * flipCost)
        return ans
