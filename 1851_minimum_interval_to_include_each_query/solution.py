# LeetCode 1851 - Minimum Interval to Include Each Query
# https://leetcode.com/problems/minimum-interval-to-include-each-query/

import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        indexed_queries = sorted(enumerate(queries), key=lambda item: item[1])
        heap: list[tuple[int, int]] = []
        answer = [-1] * len(queries)
        interval_idx = 0

        for query_idx, query in indexed_queries:
            while interval_idx < len(intervals) and intervals[interval_idx][0] <= query:
                left, right = intervals[interval_idx]
                heapq.heappush(heap, (right - left + 1, right))
                interval_idx += 1

            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            if heap:
                answer[query_idx] = heap[0][0]

        return answer
