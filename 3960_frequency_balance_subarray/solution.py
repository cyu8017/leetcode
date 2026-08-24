# LeetCode 3960 - Frequency Balance Subarray
# https://leetcode.com/problems/frequency-balance-subarray/

from typing import List


class Solution:
    def getLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        for l in range(n):
            cnt = {}
            freq = {}
            for r in range(l, n):
                x = nums[r]
                c = cnt.get(x, 0)
                if freq.get(c, 0) > 0:
                    fc = freq[c] - 1
                    if fc == 0:
                        del freq[c]
                    else:
                        freq[c] = fc
                cnt[x] = c + 1
                freq[cnt[x]] = freq.get(cnt[x], 0) + 1
                cx = cnt[x]
                if len(cnt) == 1 or (
                    len(freq) == 2
                    and (freq.get(cx * 2, 0) > 0 or (cx % 2 == 0 and freq.get(cx // 2, 0) > 0))
                ):
                    ans = max(ans, r - l + 1)
        return ans
