from collections import defaultdict
from itertools import product
from typing import List

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        parent = {}
        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        for a, b in synonyms:
            ra, rb = find(a), find(b)
            parent[ra] = rb
        groups = defaultdict(list)
        for word in parent:
            groups[find(word)].append(word)
        choices = [sorted(groups[find(w)]) if w in parent else [w] for w in text.split()]
        return [" ".join(words) for words in product(*choices)]
