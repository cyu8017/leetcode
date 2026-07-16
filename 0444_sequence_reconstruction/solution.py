# LeetCode 0444 - Sequence Reconstruction
# https://leetcode.com/problems/sequence-reconstruction/

from collections import deque


class Solution:
    def sequenceReconstruction(self, nums: list[int], sequences: list[list[int]]) -> bool:
        indegree = {value: 0 for value in nums}
        graph = {value: set() for value in nums}
        seen_edges: set[tuple[int, int]] = set()

        for sequence in sequences:
            for index in range(len(sequence) - 1):
                left, right = sequence[index], sequence[index + 1]
                if (left, right) in seen_edges:
                    continue
                seen_edges.add((left, right))
                graph[left].add(right)
                indegree[right] += 1

        queue = deque(value for value in nums if indegree[value] == 0)
        order: list[int] = []
        while queue:
            if len(queue) > 1:
                return False
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order == nums
