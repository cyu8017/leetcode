from typing import List, Optional

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        return next((i for i, w in enumerate(sentence.split(), 1)
                     if w.startswith(searchWord)), -1)
