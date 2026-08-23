// LeetCode 3608 - Minimum Time for K Connected Components
// https://leetcode.com/problems/minimum-time-for-k-connected-components/

#include <algorithm>
#include <vector>

class Solution {
    struct UnionFind {
        std::vector<int> p, size;
        UnionFind(int n) : p(n), size(n, 1) {
            for (int i = 0; i < n; i++) p[i] = i;
        }
        int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
        bool unite(int a, int b) {
            int pa = find(a), pb = find(b);
            if (pa == pb) return false;
            if (size[pa] > size[pb]) {
                p[pb] = pa;
                size[pa] += size[pb];
            } else {
                p[pa] = pb;
                size[pb] += size[pa];
            }
            return true;
        }
    };

public:
    int minTime(int n, std::vector<std::vector<int>>& edges, int k) {
        std::sort(edges.begin(), edges.end(), [](auto& a, auto& b) { return a[2] < b[2]; });
        UnionFind uf(n);
        int cnt = n;
        for (int i = (int)edges.size() - 1; i >= 0; i--) {
            if (uf.unite(edges[i][0], edges[i][1])) {
                cnt--;
                if (cnt < k) return edges[i][2];
            }
        }
        return 0;
    }
};
