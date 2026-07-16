from typing import List

class BSTIterator:
    def __init__(self, root):
        self.values = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            self.values.append(root.val)
            root = root.right
        self.index = -1
    def hasNext(self) -> bool:
        return self.index + 1 < len(self.values)
    def next(self) -> int:
        self.index += 1
        return self.values[self.index]
    def hasPrev(self) -> bool:
        return self.index > 0
    def prev(self) -> int:
        self.index -= 1
        return self.values[self.index]
