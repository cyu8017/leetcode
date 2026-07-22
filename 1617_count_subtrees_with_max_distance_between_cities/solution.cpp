// LeetCode 1617 - Count Subtrees With Max Distance Between Cities
// https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

#include <algorithm>
#include <queue>
#include <unordered_map>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> countSubgraphsForEachDiameter(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> adj(n);
        for (const auto& e : edges) {
            adj[e[0] - 1].push_back(e[1] - 1);
            adj[e[1] - 1].push_back(e[0] - 1);
        }
        std::vector<int> ans(n - 1, 0);
        for (int mask = 1; mask < (1 << n); ++mask) {
            if ((mask & (mask - 1)) == 0) {
                continue;
            }
            int start = 0;
            while (((mask >> start) & 1) == 0) {
                ++start;
            }
            auto bfs = [&](int src) {
                std::unordered_map<int, int> dist;
                std::queue<int> q;
                dist[src] = 0;
                q.push(src);
                while (!q.empty()) {
                    int u = q.front();
                    q.pop();
                    for (int v : adj[u]) {
                        if ((mask >> v) & 1 && !dist.count(v)) {
                            dist[v] = dist[u] + 1;
                            q.push(v);
                        }
                    }
                }
                int far = src;
                for (const auto& [node, d] : dist) {
                    if (d > dist[far]) {
                        far = node;
                    }
                }
                return std::make_pair(far, dist);
            };
            auto [far, seen] = bfs(start);
            if (static_cast<int>(seen.size()) == __builtin_popcount(mask)) {
                auto [_, dist] = bfs(far);
                int mx = 0;
                for (const auto& [node, d] : dist) {
                    mx = std::max(mx, d);
                }
                ++ans[mx - 1];
            }
        }
        return ans;
    }
};
