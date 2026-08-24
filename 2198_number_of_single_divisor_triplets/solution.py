# LeetCode 2198 - Number of Single Divisor Triplets
# https://leetcode.com/problems/number-of-single-divisor-triplets/

from typing import List
class Solution:
    def singleDivisorTriplet(self, nums: List[int]) -> int:
        freq = [0] * (101)
        for x in nums:
            freq[x] += 1
        ans = 0
        for a in range(1, (100) + 1):
            if not freq[a]:
                continue
            for b in range(a, (100) + 1):
                if not freq[b]:
                    continue
                for c in range(b, (100) + 1):
                    if not freq[c]:
                        continue
                    s = a + b + c
                    cnt = 0
                    if s % a == 0:
                        cnt += 1
                    if s % b == 0:
                        cnt += 1
                    if s % c == 0:
                        cnt += 1
                    if cnt != 1:
                        continue
                    if a == b and b == c:
                        ans += freq[a] * (freq[a] - 1) * (freq[a] - 2)
                    elif a == b:
                        ans += freq[a] * (freq[a] - 1) * freq[c] * 3
                    elif b == c:
                        ans += freq[b] * (freq[b] - 1) * freq[a] * 3
                    elif a == c:
                        ans += freq[a] * (freq[a] - 1) * freq[b] * 3
                    else:
                        ans += freq[a] * freq[b] * freq[c] * 6
        return ans
