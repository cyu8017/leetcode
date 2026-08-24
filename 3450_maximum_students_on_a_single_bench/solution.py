# LeetCode 3450 - Maximum Students on a Single Bench
# https://leetcode.com/problems/maximum-students-on-a-single-bench/

from typing import List


class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        bench = {}
        for s in students:
            if s[1] not in bench:
                bench[s[1]] = set()
            bench[s[1]].add(s[0])
        ans = 0
        for st in bench.values():
            if len(st) > ans:
                ans = len(st)
        return ans
