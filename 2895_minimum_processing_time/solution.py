# LeetCode 2895 - Minimum Processing Time
# https://leetcode.com/problems/minimum-processing-time/

from typing import List


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime = sorted(processorTime)
        tasks = sorted(tasks, reverse=True)
        ans = 0
        for i in range(len(processorTime)):
            fin = processorTime[i] + tasks[i * 4]
            if fin > ans:
                ans = fin
        return ans
