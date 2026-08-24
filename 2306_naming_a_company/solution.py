# LeetCode 2306 - Naming a Company
# https://leetcode.com/problems/naming-a-company/

from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups = [set() for _ in range(26)]
        for idea in ideas:
            groups[ord(idea[0]) - 97].add(idea[1:])
        ans = 0
        for i in range(26):
            for j in range(i + 1, 26):
                overlap = 0
                for s in groups[i]:
                    if s in groups[j]:
                        overlap += 1
                ans += (len(groups[i]) - overlap) * (len(groups[j]) - overlap) * 2
        return ans
