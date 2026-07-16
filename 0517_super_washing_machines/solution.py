# LeetCode 0517 - Super Washing Machines
# https://leetcode.com/problems/super-washing-machines/

class Solution:
    def findMinMoves(self, machines: list[int]) -> int:
        total = sum(machines)
        count = len(machines)
        if total % count:
            return -1
        target = total // count
        prefix = 0
        result = 0
        for clothes in machines:
            diff = clothes - target
            prefix += diff
            result = max(result, abs(prefix), diff)
        return result
