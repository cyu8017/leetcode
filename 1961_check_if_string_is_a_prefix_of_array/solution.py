from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        built = []
        for w in words:
            built.append(w)
            cur = "".join(built)
            if cur == s:
                return True
            if len(cur) > len(s) or not s.startswith(cur):
                return False
        return False
