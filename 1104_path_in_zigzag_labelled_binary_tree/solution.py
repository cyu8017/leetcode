# LeetCode 1104 - Path In Zigzag Labelled Binary Tree
# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

class Solution:
    def pathInZigZagTree(self, label: int) -> list[int]:
        path = [label]
        while label > 1:
            level = label.bit_length() - 1
            label >>= 1
            label = (1 << level) - 1 - label + (1 << (level - 1))
            path.append(label)
        return path[::-1]
