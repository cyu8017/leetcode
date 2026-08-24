# LeetCode 2122 - Recover the Original Array
# https://leetcode.com/problems/recover-the-original-array/

from typing import List
class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        n = len(nums)
        for i in range(1, n):
            diff = nums[i] - nums[0]
            if diff == 0 or diff % 2 != 0:
                continue
            k = diff / 2
            used = [False] * (n)
            used[0] = used[i] = True
            ans = [(nums[0] + nums[i]) / 2]
            l = 0
            r = i
            ok = True
            while len(ans) < n / 2:
                while l < n and used[l]:
                    l += 1
                if l == n:
                    ok = False
                    break
                need = nums[l] + 2 * k
                while r < n and (used[r] or nums[r] < need):
                    r += 1
                if r == n or nums[r] != need:
                    ok = False
                    break
                used[l] = used[r] = True
                ans.append(nums[l] + k)
            if ok:
                return ans
        return []
