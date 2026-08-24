# LeetCode 2296 - Design a Text Editor
# https://leetcode.com/problems/design-a-text-editor/


class TextEditor:
    def __init__(self):
        self.left = []
        self.right = []

    def suffix(self) -> str:
        start = max(0, len(self.left) - 10)
        return "".join(self.left[start:])

    def addText(self, text: str) -> None:
        for c in text:
            self.left.append(c)

    def deleteText(self, k: int) -> int:
        deleted = 0
        while k > 0 and self.left:
            self.left.pop()
            k -= 1
            deleted += 1
        return deleted

    def cursorLeft(self, k: int) -> str:
        while k > 0 and self.left:
            self.right.append(self.left.pop())
            k -= 1
        return self.suffix()

    def cursorRight(self, k: int) -> str:
        while k > 0 and self.right:
            self.left.append(self.right.pop())
            k -= 1
        return self.suffix()
