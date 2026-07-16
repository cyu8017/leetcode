class Solution:
    def countPairs(self, n, edges, queries):
        from collections import Counter
        deg = [0] * (n + 1)
        shared = Counter()
        for a, b in edges:
            if a > b:
                a, b = b, a
            deg[a] += 1
            deg[b] += 1
            shared[(a, b)] += 1
        freq = Counter()
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                freq[deg[a] + deg[b]] += 1
                freq[deg[a] + deg[b] - shared[(a, b)]] -= 1
        total = [0] * (2 * len(edges) + 2)
        running = 0
        for k in range(len(total)):
            running += freq[k]
            total[k] = running
        return [total[q] for q in queries]
