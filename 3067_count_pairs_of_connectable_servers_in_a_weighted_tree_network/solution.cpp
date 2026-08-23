// LeetCode 3067 - Count Pairs of Connectable Servers in a Weighted Tree Network
// https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

#include <functional>
#include <vector>

class Solution {
public:
    std::vector<int> countPairsOfConnectableServers(std::vector<std::vector<int>>& edges, int signalSpeed) {
        int n = (int)edges.size() + 1;
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
        }
        std::function<int(int, int, int)> dfs = [&](int a, int fa, int ws) {
            int cnt = (ws % signalSpeed == 0) ? 1 : 0;
            for (auto [b, w] : g[a])
                if (b != fa) cnt += dfs(b, a, ws + w);
            return cnt;
        };
        std::vector<int> ans(n);
        for (int a = 0; a < n; a++) {
            int s = 0;
            for (auto [b, w] : g[a]) {
                int t = dfs(b, a, w);
                ans[a] += s * t;
                s += t;
            }
        }
        return ans;
    }
};
