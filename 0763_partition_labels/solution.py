# LeetCode 0763 - Partition Labels
# https://leetcode.com/problems/partition-labels/

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {ch: i for i, ch in enumerate(s)}
        start = end = 0
        answer: list[int] = []
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                answer.append(end - start + 1)
                start = i + 1
        return answer
