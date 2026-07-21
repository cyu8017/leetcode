from bisect import bisect_left
from typing import List

class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
        nodes = []  # sorted (value, depth)
        ans = 0
        for value in order:
            i = bisect_left(nodes, (value, 0))
            depth = 1
            if i:
                depth = max(depth, nodes[i - 1][1] + 1)
            if i < len(nodes):
                depth = max(depth, nodes[i][1] + 1)
            nodes.insert(i, (value, depth))
            ans = max(ans, depth)
        return ans
