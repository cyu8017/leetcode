# LeetCode 0558 - Logical OR of Two Binary Grids Represented as Quad-Trees
# https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/


class Node:
    def __init__(
        self,
        val: bool = False,
        isLeaf: bool = False,
        topLeft: "Node | None" = None,
        topRight: "Node | None" = None,
        bottomLeft: "Node | None" = None,
        bottomRight: "Node | None" = None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: "Node", quadTree2: "Node") -> "Node":
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1

        top_left = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        top_right = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottom_left = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottom_right = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        if (
            top_left.isLeaf
            and top_right.isLeaf
            and bottom_left.isLeaf
            and bottom_right.isLeaf
            and top_left.val == top_right.val == bottom_left.val == bottom_right.val
        ):
            return Node(top_left.val, True)

        return Node(False, False, top_left, top_right, bottom_left, bottom_right)
