// LeetCode 3820 - Pythagorean Distance Nodes In A Tree
// https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/

#include <algorithm>
#include <cstdint>
#include <queue>
#include <vector>

class Solution {
public:
    int specialNodes(int n, std::vector<std::vector<int>>& edges, int x, int y, int z) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        const int INF = 1e9;
        auto bfs = [&](int start) {
            std::vector<int> dist(n, INF);
            std::queue<int> q;
            dist[start] = 0;
            q.push(start);
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                for (int v : g[u]) {
                    if (dist[v] > dist[u] + 1) {
                        dist[v] = dist[u] + 1;
                        q.push(v);
                    }
                }
            }
            return dist;
        };
        auto d1 = bfs(x), d2 = bfs(y), d3 = bfs(z);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int a[3] = {d1[i], d2[i], d3[i]};
            std::sort(a, a + 3);
            int64_t x0 = a[0], x1 = a[1], x2 = a[2];
            if (x0 * x0 + x1 * x1 == x2 * x2) ans++;
        }
        return ans;
    }
};
