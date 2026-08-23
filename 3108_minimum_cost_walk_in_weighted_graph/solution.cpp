// LeetCode 3108 - Minimum Cost Walk in Weighted Graph
// https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

#include <vector>

class Solution {
    struct UnionFind {
        std::vector<int> p, size;
        explicit UnionFind(int n) : p(n), size(n, 1) {
            for (int i = 0; i < n; i++) p[i] = i;
        }
        int find(int x) {
            if (p[x] != x) p[x] = find(p[x]);
            return p[x];
        }
        void unite(int a, int b) {
            int pa = find(a), pb = find(b);
            if (pa == pb) return;
            if (size[pa] > size[pb]) {
                p[pb] = pa;
                size[pa] += size[pb];
            } else {
                p[pa] = pb;
                size[pb] += size[pa];
            }
        }
    };
public:
    std::vector<int> minimumCost(int n, std::vector<std::vector<int>>& edges, std::vector<std::vector<int>>& query) {
        UnionFind uf(n);
        std::vector<int> g(n, -1);
        for (auto& e : edges) uf.unite(e[0], e[1]);
        for (auto& e : edges) {
            int root = uf.find(e[0]);
            g[root] &= e[2];
        }
        auto f = [&](int u, int v) {
            if (u == v) return 0;
            int a = uf.find(u), b = uf.find(v);
            if (a == b) return g[a];
            return -1;
        };
        std::vector<int> ans;
        for (auto& q : query) ans.push_back(f(q[0], q[1]));
        return ans;
    }
};
