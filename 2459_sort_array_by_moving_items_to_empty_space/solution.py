# LeetCode 2459 - Sort Array By Moving Items to Empty Space
# https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> int:
        def solve_one(start_zero: bool) -> int:
            n = len(nums)
            arr = nums[:]
            pos = {arr[i]: i for i in range(n)}
            ops = 0
            while True:
                empty = pos[0]
                should = empty if start_zero else (0 if empty == n - 1 else empty + 1)
                if arr[empty] == should:
                    found = -1
                    for i in range(n):
                        want = i if start_zero else (0 if i == n - 1 else i + 1)
                        if arr[i] != want:
                            found = i
                            break
                    if found == -1:
                        return ops
                    v = arr[found]
                    arr[empty] = arr[found]
                    arr[found] = 0
                    pos[0] = found
                    pos[v] = empty
                    ops += 1
                    continue
                j = pos[should]
                vv = arr[j]
                arr[empty] = arr[j]
                arr[j] = 0
                pos[0] = j
                pos[vv] = empty
                ops += 1

        return min(solve_one(True), solve_one(False))
