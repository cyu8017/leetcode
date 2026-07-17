# LeetCode 1889 - Minimum Space Wasted From Packaging
# https://leetcode.com/problems/minimum-space-wasted-from-packaging/

import bisect
from itertools import accumulate
from typing import List


class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        prefix = list(accumulate(packages))
        answer = float("inf")

        for supplier in boxes:
            supplier.sort()
            start = 0
            wasted = 0

            for box in supplier:
                end = bisect.bisect_right(packages, box, lo=start)
                if end == start:
                    continue
                package_sum = prefix[end - 1] - (prefix[start - 1] if start else 0)
                wasted += box * (end - start) - package_sum
                start = end

            if start == len(packages):
                answer = min(answer, wasted)

        return -1 if answer == float("inf") else answer % 1_000_000_007
