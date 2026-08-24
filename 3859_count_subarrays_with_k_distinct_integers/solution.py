# LeetCode 3859 - Count Subarrays With K Distinct Integers
# https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

from typing import Dict, List


class Solution:
    def countSubarrays(self, nums: List[int], k: int, m: int) -> int:
        def f(lim: int) -> int:
            cnt: Dict[int, int] = {}
            ans = 0
            l = 0
            t = 0
            for x in nums:
                c = cnt.get(x, 0) + 1
                cnt[x] = c
                if c == m:
                    t += 1
                while len(cnt) >= lim and t >= k:
                    y = nums[l]
                    l += 1
                    cy = cnt[y] - 1
                    if cy == m - 1:
                        t -= 1
                    if cy == 0:
                        del cnt[y]
                    else:
                        cnt[y] = cy
                ans += l
            return ans

        return f(k) - f(k + 1)
