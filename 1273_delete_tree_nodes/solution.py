from typing import List

class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        children = [[] for _ in range(nodes)]
        for node in range(1, nodes):
            children[parent[node]].append(node)
        def dfs(node):
            total, count = value[node], 1
            for child in children[node]:
                child_sum, child_count = dfs(child)
                total += child_sum
                count += child_count
            return (total, 0 if total == 0 else count)
        return dfs(0)[1]
