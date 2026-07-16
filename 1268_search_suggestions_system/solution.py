from bisect import bisect_left
from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        answer, prefix = [], ""
        for ch in searchWord:
            prefix += ch
            i = bisect_left(products, prefix)
            answer.append([p for p in products[i:i + 3] if p.startswith(prefix)])
        return answer
