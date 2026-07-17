from collections import Counter

class Solution:
    def countPairs(self, n, edges, queries):
        deg = [0] * (n + 1)
        shared = Counter()
        for a, b in edges:
            if a > b:
                a, b = b, a
            deg[a] += 1
            deg[b] += 1
            shared[(a, b)] += 1
        sorted_deg = sorted(deg[1:])
        ans = []
        for q in queries:
            res = 0
            left, right = 0, n - 1
            while left < right:
                if sorted_deg[left] + sorted_deg[right] > q:
                    res += right - left
                    right -= 1
                else:
                    left += 1
            for (a, b), count in shared.items():
                if deg[a] + deg[b] > q >= deg[a] + deg[b] - count:
                    res -= 1
            ans.append(res)
        return ans
