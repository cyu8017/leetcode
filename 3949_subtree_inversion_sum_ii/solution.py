# LeetCode 3949 - Subtree Inversion Sum II
# https://leetcode.com/problems/subtree-inversion-sum-ii/

from typing import List


class Solution:
    def maxSubtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        parent = [-2] * n
        parent[0] = -1
        order = [0]
        i = 0
        while i < len(order):
            u = order[i]
            for v in graph[u]:
                if parent[v] == -2:
                    parent[v] = u
                    order.append(v)
            i += 1
        infinity = 2 ** 60
        maximum = [None] * n
        minimum = [None] * n
        for oi in range(n - 1, -1, -1):
            u = order[oi]
            current_max = [-infinity] * (k + 1)
            current_min = [infinity] * (k + 1)
            current_max[k] = current_min[k] = nums[u]
            for v in graph[u]:
                if parent[v] != u:
                    continue
                next_max = [-infinity] * (k + 1)
                next_min = [infinity] * (k + 1)
                for first in range(k + 1):
                    if current_max[first] == -infinity:
                        continue
                    for child_distance in range(k + 1):
                        if maximum[v][child_distance] == -infinity:
                            continue
                        second = child_distance + 1
                        if second > k:
                            second = k
                        if first < k and second < k and first + second < k:
                            continue
                        distance = min(first, second)
                        max_value = current_max[first] + maximum[v][child_distance]
                        min_value = current_min[first] + minimum[v][child_distance]
                        next_max[distance] = max(next_max[distance], max_value)
                        next_min[distance] = min(next_min[distance], min_value)
                current_max = next_max
                current_min = next_min
            if -current_min[k] > current_max[0]:
                current_max[0] = -current_min[k]
            if -current_max[k] < current_min[0]:
                current_min[0] = -current_max[k]
            maximum[u] = current_max
            minimum[u] = current_min
        answer = -(2 ** 60)
        for value in maximum[0]:
            answer = max(answer, value)
        return answer
