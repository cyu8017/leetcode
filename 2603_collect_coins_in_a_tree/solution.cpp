// LeetCode 2603 - Collect Coins in a Tree
// https://leetcode.com/problems/collect-coins-in-a-tree/

#include <queue>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int collectTheCoins(std::vector<int>& coins, std::vector<std::vector<int>>& edges) {
        int n = (int)coins.size();
        std::vector<std::unordered_set<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].insert(e[1]);
            g[e[1]].insert(e[0]);
        }
        std::vector<int> deg(n);
        for (int i = 0; i < n; ++i) deg[i] = (int)g[i].size();
        std::queue<int> q;
        for (int i = 0; i < n; ++i) {
            if (deg[i] == 1 && coins[i] == 0) q.push(i);
        }
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : std::vector<int>(g[u].begin(), g[u].end())) {
                g[v].erase(u);
                deg[v]--;
                if (deg[v] == 1 && coins[v] == 0) q.push(v);
            }
            g[u].clear();
            deg[u] = 0;
        }
        for (int round = 0; round < 2; ++round) {
            std::vector<int> leaves;
            for (int i = 0; i < n; ++i) if (deg[i] == 1) leaves.push_back(i);
            for (int u : leaves) {
                for (int v : std::vector<int>(g[u].begin(), g[u].end())) {
                    g[v].erase(u);
                    deg[v]--;
                }
                g[u].clear();
                deg[u] = 0;
            }
        }
        int remain = 0;
        for (int i = 0; i < n; ++i) remain += (int)g[i].size();
        return remain;
    }
};
