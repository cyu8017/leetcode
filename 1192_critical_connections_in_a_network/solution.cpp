// LeetCode 1192 - Critical Connections in a Network
// https://leetcode.com/problems/critical-connections-in-a-network/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> criticalConnections(int n, std::vector<std::vector<int>>& connections) {
        std::vector<std::vector<int>> graph(n);
        for (const auto& e : connections) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }
        std::vector<int> disc(n, -1), low(n, -1);
        std::vector<std::vector<int>> bridges;
        int timer = 0;
        auto dfs = [&](auto&& self, int node, int parent) -> void {
            disc[node] = low[node] = timer++;
            for (int nxt : graph[node]) {
                if (nxt == parent) continue;
                if (disc[nxt] == -1) {
                    self(self, nxt, node);
                    low[node] = std::min(low[node], low[nxt]);
                    if (low[nxt] > disc[node]) bridges.push_back({std::min(node, nxt), std::max(node, nxt)});
                } else {
                    low[node] = std::min(low[node], disc[nxt]);
                }
            }
        };
        dfs(dfs, 0, -1);
        return bridges;
    }
};
