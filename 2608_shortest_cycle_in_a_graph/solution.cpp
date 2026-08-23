// LeetCode 2608 - Shortest Cycle in a Graph
// https://leetcode.com/problems/shortest-cycle-in-a-graph/

#include <queue>
#include <vector>

class Solution {
public:
    int findShortestCycle(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        const int INF = 1e9;
        int ans = INF;
        for (int start = 0; start < n; ++start) {
            std::vector<int> dist(n, -1), parent(n, -1);
            std::queue<int> q;
            q.push(start);
            dist[start] = 0;
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                for (int v : g[u]) {
                    if (dist[v] < 0) {
                        dist[v] = dist[u] + 1;
                        parent[v] = u;
                        q.push(v);
                    } else if (parent[u] != v) {
                        int c = dist[u] + dist[v] + 1;
                        if (c < ans) ans = c;
                    }
                }
            }
        }
        return ans == INF ? -1 : ans;
    }
};
