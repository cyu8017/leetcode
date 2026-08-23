// LeetCode 1761 - Minimum Degree of a Connected Trio in a Graph
// https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minTrioDegree(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<bool>> adj(n, std::vector<bool>(n, false));
        std::vector<int> degree(n, 0);
        for (const auto& e : edges) {
            int u = e[0] - 1;
            int v = e[1] - 1;
            adj[u][v] = true;
            adj[v][u] = true;
            degree[u]++;
            degree[v]++;
        }
        int best = INT_MAX;
        for (const auto& e : edges) {
            int u = e[0] - 1;
            int v = e[1] - 1;
            for (int k = 0; k < n; k++) {
                if (adj[u][k] && adj[v][k]) {
                    best = std::min(best, degree[u] + degree[v] + degree[k] - 6);
                }
            }
        }
        return best == INT_MAX ? -1 : best;
    }
};
