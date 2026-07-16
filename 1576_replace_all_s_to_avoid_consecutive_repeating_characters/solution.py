from typing import List

class Solution:
    def modifyString(self, s: str) -> str:
        chars = list(s)
        for i, ch in enumerate(chars):
            if ch == "?":
                chars[i] = next(c for c in "abc" if (i == 0 or chars[i - 1] != c) and (i + 1 == len(chars) or chars[i + 1] != c))
        return "".join(chars)
