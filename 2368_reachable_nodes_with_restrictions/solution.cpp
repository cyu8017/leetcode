// LeetCode 2368 - Reachable Nodes With Restrictions
// https://leetcode.com/problems/reachable-nodes-with-restrictions/

#include <queue>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int reachableNodes(int n, std::vector<std::vector<int>>& edges, std::vector<int>& restricted) {
        std::unordered_set<int> ban(restricted.begin(), restricted.end());
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        int ans = 0;
        std::vector<char> vis(n, 0);
        std::queue<int> q;
        q.push(0);
        vis[0] = 1;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            ans++;
            for (int v : g[u]) {
                if (!vis[v] && !ban.count(v)) {
                    vis[v] = 1;
                    q.push(v);
                }
            }
        }
        return ans;
    }
};
