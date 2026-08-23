// LeetCode 0684 - Redundant Connection
// https://leetcode.com/problems/redundant-connection/

#include <numeric>
#include <vector>

class Solution {
    int find(std::vector<int>& parent, int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

public:
    std::vector<int> findRedundantConnection(std::vector<std::vector<int>>& edges) {
        std::vector<int> parent(edges.size() + 1);
        std::iota(parent.begin(), parent.end(), 0);
        for (const auto& edge : edges) {
            const int u = edge[0];
            const int v = edge[1];
            const int pu = find(parent, u);
            const int pv = find(parent, v);
            if (pu == pv) {
                return {u, v};
            }
            parent[pu] = pv;
        }
        return {};
    }
};
