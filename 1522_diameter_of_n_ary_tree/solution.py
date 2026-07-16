# LeetCode 1522

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []

class Solution:
    def diameter(self, root):
        answer = 0
        def depth(node):
            nonlocal answer
            longest = second = 0
            for child in node.children:
                value = depth(child) + 1
                if value > longest:
                    longest, second = value, longest
                elif value > second:
                    second = value
            answer = max(answer, longest + second)
            return longest
        if root:
            depth(root)
        return answer
