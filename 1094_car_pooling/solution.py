# LeetCode 1094 - Car Pooling
# https://leetcode.com/problems/car-pooling/

class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        diff = [0] * 1001
        for num, start, end in trips:
            diff[start] += num
            diff[end] -= num
        cur = 0
        for x in diff:
            cur += x
            if cur > capacity:
                return False
        return True
