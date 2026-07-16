# LeetCode 0604 - Design Compressed String Iterator
# https://leetcode.com/problems/design-compressed-string-iterator/


class StringIterator:
    def __init__(self, compressedString: str):
        self.chars: list[str] = []
        self.counts: list[int] = []
        i = 0
        n = len(compressedString)
        while i < n:
            ch = compressedString[i]
            i += 1
            j = i
            while j < n and compressedString[j].isdigit():
                j += 1
            self.chars.append(ch)
            self.counts.append(int(compressedString[i:j]))
            i = j
        self.index = 0

    def next(self) -> str:
        if not self.hasNext():
            return " "
        ch = self.chars[self.index]
        self.counts[self.index] -= 1
        if self.counts[self.index] == 0:
            self.index += 1
        return ch

    def hasNext(self) -> bool:
        return self.index < len(self.chars)
