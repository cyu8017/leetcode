# LeetCode 3591 - Check if Any Element Has Prime Frequency
# https://leetcode.com/problems/check-if-any-element-has-prime-frequency/

from typing import List


def is_prime3591(x: int) -> bool:
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        cnt = {}
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1
        for v in cnt.values():
            if is_prime3591(v):
                return True
        return False
