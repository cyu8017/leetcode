#include <vector>

class Solution {
    std::vector<std::vector<int>> g;
    double dfs(int u, int p, int time, int t, int target, double prob) {
        std::vector<int> kids;
        for (int v : g[u]) if (v != p) kids.push_back(v);
        if (time == t || kids.empty()) return u == target ? prob : 0.0;
        double ans = 0;
        for (int v : kids) ans += dfs(v, u, time + 1, t, target, prob / kids.size());
        return ans;
    }
public:
    double frogPosition(int n, std::vector<std::vector<int>>& edges, int t, int target) {
        g.assign(n + 1, {});
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        return dfs(1, 0, 0, t, target, 1.0);
    }
};
