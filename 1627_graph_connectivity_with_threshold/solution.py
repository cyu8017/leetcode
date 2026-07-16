class Solution:
    def areConnected(self, n, threshold, queries):
        parent = list(range(n + 1))
        def find(x):
            while x != parent[x]: parent[x] = parent[parent[x]]; x = parent[x]
            return x
        for d in range(threshold + 1, n + 1):
            for x in range(2*d, n + 1, d):
                a, b = find(d), find(x)
                if a != b: parent[b] = a
        return [find(a) == find(b) for a, b in queries]
