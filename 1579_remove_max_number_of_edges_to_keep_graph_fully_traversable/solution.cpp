// LeetCode 1579 - Remove Max Number of Edges to Keep Graph Fully Traversable
// https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

#include <vector>

class DSU {
public:
    std::vector<int> parent;
    int components;

    explicit DSU(int n) : parent(n + 1), components(n) {
        for (int i = 0; i <= n; ++i) {
            parent[i] = i;
        }
    }

    int find(int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    bool unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) {
            return false;
        }
        parent[a] = b;
        --components;
        return true;
    }
};

class Solution {
public:
    int maxNumEdgesToRemove(int n, std::vector<std::vector<int>>& edges) {
        DSU alice(n);
        DSU bob(n);
        int used = 0;
        for (const auto& edge : edges) {
            if (edge[0] == 3) {
                const bool merged = alice.unite(edge[1], edge[2]);
                bob.unite(edge[1], edge[2]);
                used += merged;
            }
        }
        for (const auto& edge : edges) {
            if (edge[0] == 1) {
                used += alice.unite(edge[1], edge[2]);
            } else if (edge[0] == 2) {
                used += bob.unite(edge[1], edge[2]);
            }
        }
        return (alice.components == 1 && bob.components == 1)
                   ? static_cast<int>(edges.size()) - used
                   : -1;
    }
};
