from typing import List

class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        spaces = text.count(" ")
        if len(words) == 1:
            return words[0] + " " * spaces
        between, trailing = divmod(spaces, len(words) - 1)
        return (" " * between).join(words) + " " * trailing
