# LeetCode 3267 - Count Almost Equal Pairs II
# https://leetcode.com/problems/count-almost-equal-pairs-ii/

from typing import List


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        sa = sb = ""

        def padNum(x: int) -> str:
            return str(x)

        def dfs(arr: List[str], start: int, left: int) -> bool:
            if "".join(arr) == sb:
                return True
            if left == 0:
                return False
            for i in range(start, len(arr)):
                if arr[i] == sb[i]:
                    continue
                for j in range(i + 1, len(arr)):
                    if arr[j] == sb[i]:
                        arr[i], arr[j] = arr[j], arr[i]
                        if dfs(arr, i + 1, left - 1):
                            return True
                        arr[i], arr[j] = arr[j], arr[i]
                return False
            return "".join(arr) == sb

        def almostEqual(a: int, b: int) -> bool:
            nonlocal sa, sb
            sa, sb = padNum(a), padNum(b)
            while len(sa) < len(sb):
                sa = "0" + sa
            while len(sb) < len(sa):
                sb = "0" + sb
            if sa == sb:
                return True
            return dfs(list(sa), 0, 2)

        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if almostEqual(nums[i], nums[j]):
                    ans += 1
        return ans
