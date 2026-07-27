// LeetCode 1059 - All Paths from Source Lead to Destination
// https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

#include <functional>
#include <vector>

class Solution {
public:
    bool leadsToDestination(int n, std::vector<std::vector<int>>& edges, int source, int destination) {
        std::vector<std::vector<int>> graph(n);
        for (const auto& e : edges) {
            graph[e[0]].push_back(e[1]);
        }
        std::vector<int> state(n, 0);

        std::function<bool(int)> dfs = [&](int node) -> bool {
            if (graph[node].empty()) {
                return node == destination;
            }
            if (state[node] == 1) {
                return false;
            }
            if (state[node] == 2) {
                return true;
            }
            state[node] = 1;
            for (int nxt : graph[node]) {
                if (!dfs(nxt)) {
                    return false;
                }
            }
            state[node] = 2;
            return true;
        };

        return dfs(source);
    }
};
