// LeetCode 3243 - Shortest Distance After Road Addition Queries I
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

#include <queue>
#include <vector>

class Solution {
public:
    std::vector<int> shortestDistanceAfterQueries(int n, std::vector<std::vector<int>>& queries) {
        std::vector<std::vector<int>> g(n);
        for (int i = 0; i < n - 1; i++) g[i].push_back(i + 1);
        auto bfs = [&](int start) {
            std::queue<int> q;
            q.push(start);
            std::vector<char> vis(n, 0);
            vis[start] = 1;
            for (int d = 0;; d++) {
                int k = (int)q.size();
                while (k--) {
                    int u = q.front();
                    q.pop();
                    if (u == n - 1) return d;
                    for (int v : g[u]) {
                        if (!vis[v]) {
                            vis[v] = 1;
                            q.push(v);
                        }
                    }
                }
            }
        };
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            g[queries[i][0]].push_back(queries[i][1]);
            ans[i] = bfs(0);
        }
        return ans;
    }
};
