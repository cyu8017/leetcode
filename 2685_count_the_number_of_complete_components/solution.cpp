// LeetCode 2685 - Count the Number of Complete Components
// https://leetcode.com/problems/count-the-number-of-complete-components/

#include <vector>
#include <functional>

class Solution {
public:
    int countCompleteComponents(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) { g[e[0]].push_back(e[1]); g[e[1]].push_back(e[0]); }
        std::vector<char> vis(n);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (vis[i]) continue;
            std::vector<int> nodes;
            std::function<void(int)> dfs = [&](int u) {
                vis[u] = 1; nodes.push_back(u);
                for (int v : g[u]) if (!vis[v]) dfs(v);
            };
            dfs(i);
            int ecount = 0;
            for (int u : nodes) ecount += (int)g[u].size();
            ecount /= 2;
            int sz = (int)nodes.size();
            if (ecount == sz * (sz - 1) / 2) ans++;
        }
        return ans;
    }
};
