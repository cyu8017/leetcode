# LeetCode 3984 - Divisible Game
# https://leetcode.com/problems/divisible-game/

from typing import List


class Solution:
    def divisibleGame(self, nums: List[int]) -> int:
        candidates = set()
        candidates.add(2)
        for value in nums:
            divisor = 2
            while divisor * divisor <= value:
                if value % divisor == 0:
                    candidates.add(divisor)
                    candidates.add(value // divisor)
                divisor += 1
            if value > 1:
                candidates.add(value)
        best_score = -(1 << 62)
        best_k = 0
        for k in candidates:
            ending = 0
            score = 0
            for i in range(len(nums)):
                value = nums[i]
                contribution = -value
                if value % k == 0:
                    contribution = value
                if i == 0 or ending + contribution < contribution:
                    ending = contribution
                else:
                    ending += contribution
                if i == 0 or ending > score:
                    score = ending
            if score > best_score or (score == best_score and k < best_k):
                best_score = score
                best_k = k
        mod = 1000000007
        answer = (best_score % mod) * best_k % mod
        if answer < 0:
            answer += mod
        return answer
