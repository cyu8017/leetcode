# LeetCode 3944 - Minimum Operations to Make Array Modulo Alternating II
# https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/

from typing import List


def costs(freq: List[int], k: int) -> List[int]:
    dbl = [0] * (2 * k)
    for i in range(2 * k):
        dbl[i] = freq[i % k]
    count_prefix = [0] * (2 * k + 1)
    weighted_prefix = [0] * (2 * k + 1)
    for i in range(2 * k):
        count_prefix[i + 1] = count_prefix[i] + dbl[i]
        weighted_prefix[i + 1] = weighted_prefix[i] + i * dbl[i]
    res = [0] * k
    cw = k // 2
    cc = (k - 1) // 2
    for t in range(k):
        cnt = count_prefix[t + cw + 1] - count_prefix[t]
        s = weighted_prefix[t + cw + 1] - weighted_prefix[t]
        res[t] += s - t * cnt
        if cc > 0:
            cnt2 = count_prefix[t + k] - count_prefix[t + k - cc]
            sum2 = weighted_prefix[t + k] - weighted_prefix[t + k - cc]
            res[t] += (t + k) * cnt2 - sum2
    return res


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        even_freq = [0] * k
        odd_freq = [0] * k
        for i in range(len(nums)):
            if i % 2 == 0:
                even_freq[nums[i] % k] += 1
            else:
                odd_freq[nums[i] % k] += 1
        even_cost = costs(even_freq, k)
        odd_cost = costs(odd_freq, k)
        best1 = 1 << 62
        best2 = 1 << 62
        best_index = -1
        for i in range(k):
            x = odd_cost[i]
            if x < best1:
                best2 = best1
                best1 = x
                best_index = i
            elif x < best2:
                best2 = x
        ans = 1 << 62
        for x in range(k):
            other = best2 if x == best_index else best1
            ans = min(ans, even_cost[x] + other)
        return ans
