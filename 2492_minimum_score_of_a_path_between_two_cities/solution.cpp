// LeetCode 2492 - Minimum Score of a Path Between Two Cities
// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int minScore(int n, std::vector<std::vector<int>>& roads) {
        std::vector<std::vector<std::pair<int, int>>> g(n + 1);
        for (auto& r : roads) {
            g[r[0]].push_back({r[1], r[2]});
            g[r[1]].push_back({r[0], r[2]});
        }
        std::vector<char> vis(n + 1);
        int ans = 1 << 30;
        std::queue<int> q;
        q.push(1);
        vis[1] = 1;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (auto [v, w] : g[u]) {
                if (w < ans) ans = w;
                if (!vis[v]) {
                    vis[v] = 1;
                    q.push(v);
                }
            }
        }
        return ans;
    }
};
