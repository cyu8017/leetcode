# LeetCode 2764 - Is Array a Preorder of Some Binary Tree
# https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/

from typing import List


class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        if not nodes:
            return True
        stack = [nodes[0][0]]
        for i in range(1, len(nodes)):
            node_id, parent = nodes[i][0], nodes[i][1]
            while stack and stack[-1] != parent:
                stack.pop()
            if not stack:
                return False
            stack.append(node_id)
        return True
