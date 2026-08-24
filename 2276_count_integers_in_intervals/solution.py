# LeetCode 2276 - Count Integers in Intervals
# https://leetcode.com/problems/count-integers-in-intervals/


class _Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.covered = False


class CountIntervals:
    def __init__(self):
        self.root = None
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        def add_range(L, R, l, r, node):
            if not node:
                node = _Node()
            if node.covered:
                return 0, node
            if l <= L and R <= r:
                node.covered = True
                node.left = node.right = None
                return R - L + 1, node
            mid = (L + R) // 2
            added = 0
            if l <= mid:
                extra, node.left = add_range(L, mid, l, r, node.left)
                added += extra
            if r > mid:
                extra, node.right = add_range(mid + 1, R, l, r, node.right)
                added += extra
            if node.left and node.right and node.left.covered and node.right.covered:
                node.covered = True
                node.left = node.right = None
            return added, node

        extra, self.root = add_range(1, 1000000000, left, right, self.root)
        self.cnt += extra

    def count(self) -> int:
        return self.cnt
