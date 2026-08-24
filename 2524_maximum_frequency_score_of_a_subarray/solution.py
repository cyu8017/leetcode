# LeetCode 2524 - Maximum Frequency Score of a Subarray
# https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/

from typing import List


class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        MOD = 1000000007

        def mod_pow(a: int, e: int) -> int:
            res = 1
            a %= MOD
            while e > 0:
                if e & 1:
                    res = res * a % MOD
                a = a * a % MOD
                e >>= 1
            return res

        freq = {}

        def add(score: int, x: int) -> int:
            c = freq.get(x, 0)
            if c > 0:
                score = (score - mod_pow(x, c) + MOD) % MOD
            freq[x] = c + 1
            return (score + mod_pow(x, c + 1)) % MOD

        def remove(score: int, x: int) -> int:
            c = freq[x]
            score = (score - mod_pow(x, c) + MOD) % MOD
            if c == 1:
                del freq[x]
            else:
                freq[x] = c - 1
                score = (score + mod_pow(x, c - 1)) % MOD
            return score

        score = 0
        best = 0
        for i in range(len(nums)):
            score = add(score, nums[i])
            if i >= k:
                score = remove(score, nums[i - k])
            if i >= k - 1 and score > best:
                best = score
        return best
