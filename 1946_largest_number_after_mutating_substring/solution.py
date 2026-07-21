from typing import List

class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        chars = list(num)
        started = False
        for i, ch in enumerate(chars):
            d = int(ch)
            mapped = change[d]
            if mapped > d:
                chars[i] = str(mapped)
                started = True
            elif mapped < d and started:
                break
        return ''.join(chars)
