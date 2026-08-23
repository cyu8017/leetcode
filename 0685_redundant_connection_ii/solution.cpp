// LeetCode 0685 - Redundant Connection II
// https://leetcode.com/problems/redundant-connection-ii/

#include <numeric>
#include <vector>

class Solution {
    int find(std::vector<int>& uf, int x) {
        while (uf[x] != x) {
            uf[x] = uf[uf[x]];
            x = uf[x];
        }
        return x;
    }

public:
    std::vector<int> findRedundantDirectedConnection(std::vector<std::vector<int>>& edges) {
        const int n = static_cast<int>(edges.size());
        std::vector<int> parent(n + 1, 0);
        std::vector<int> cand1;
        std::vector<int> cand2;
        for (int i = 0; i < n; ++i) {
            const int u = edges[i][0];
            const int v = edges[i][1];
            if (parent[v] == 0) {
                parent[v] = u;
            } else {
                cand1 = {parent[v], v};
                cand2 = {u, v};
                edges[i] = {-1, -1};
                break;
            }
        }

        std::vector<int> uf(n + 1);
        std::iota(uf.begin(), uf.end(), 0);
        for (const auto& edge : edges) {
            if (edge[0] < 0) {
                continue;
            }
            const int pu = find(uf, edge[0]);
            const int pv = find(uf, edge[1]);
            if (pu == pv) {
                return cand1.empty() ? std::vector<int>{edge[0], edge[1]} : cand1;
            }
            uf[pu] = pv;
        }
        return cand2;
    }
};
