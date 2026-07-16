from typing import List

class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        seen = set()
        for word in dict:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                if pattern in seen:
                    return True
                seen.add(pattern)
        return False
