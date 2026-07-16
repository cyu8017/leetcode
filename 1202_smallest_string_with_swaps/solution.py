from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        parent = list(range(len(s)))
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for a, b in pairs:
            ra, rb = find(a), find(b)
            parent[ra] = rb
        groups = defaultdict(list)
        for i, ch in enumerate(s): groups[find(i)].append(ch)
        for chars in groups.values(): chars.sort(reverse=True)
        return ''.join(groups[find(i)].pop() for i in range(len(s)))
