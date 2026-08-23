// LeetCode 3600 - Maximize Spanning Tree Stability with Upgrades
// https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

#include <algorithm>
#include <vector>

class Solution {
    struct UnionFind {
        std::vector<int> p, size;
        int cnt;
        UnionFind(int n) : p(n), size(n, 1), cnt(n) {
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
            cnt--;
            return true;
        }
    };

    int N, K;
    std::vector<std::vector<int>>* E;

    bool check(int lim) {
        UnionFind uf(N);
        for (auto& e : *E) {
            if (e[2] >= lim) uf.unite(e[0], e[1]);
        }
        int rem = K;
        for (auto& e : *E) {
            if (e[2] * 2 >= lim && rem > 0) {
                if (uf.unite(e[0], e[1])) rem--;
            }
        }
        return uf.cnt == 1;
    }

public:
    int maxStability(int n, std::vector<std::vector<int>>& edges, int k) {
        N = n;
        E = &edges;
        K = k;
        UnionFind uf(n);
        int mn = 1000000;
        for (auto& e : edges) {
            if (e[3] == 1) {
                mn = std::min(mn, e[2]);
                if (!uf.unite(e[0], e[1])) return -1;
            }
        }
        for (auto& e : edges) uf.unite(e[0], e[1]);
        if (uf.cnt > 1) return -1;
        int l = 1, r = mn;
        while (l < r) {
            int mid = (l + r + 1) >> 1;
            if (check(mid)) l = mid;
            else r = mid - 1;
        }
        return l;
    }
};
