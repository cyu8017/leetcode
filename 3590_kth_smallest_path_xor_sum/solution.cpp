// LeetCode 3590 - Kth Smallest Path XOR Sum
// https://leetcode.com/problems/kth-smallest-path-xor-sum/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> kthSmallest(std::vector<int>& par, std::vector<int>& vals, std::vector<std::vector<int>>& queries) {
        int n = (int)par.size();
        std::vector<std::vector<int>> g(n);
        for (int i = 1; i < n; i++) g[par[i]].push_back(i);
        std::vector<int> xorPath(n);
        auto dfs = [&](auto&& self, int u) -> void {
            xorPath[u] ^= vals[u];
            for (int v : g[u]) {
                xorPath[v] = xorPath[u];
                self(self, v);
            }
        };
        dfs(dfs, 0);
        std::vector<int> inT(n), outT(n), order;
        auto dfs2 = [&](auto&& self, int u) -> void {
            inT[u] = (int)order.size();
            order.push_back(xorPath[u]);
            for (int v : g[u]) self(self, v);
            outT[u] = (int)order.size();
        };
        dfs2(dfs2, 0);
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int u = queries[i][0], k = queries[i][1];
            std::vector<int> sub(order.begin() + inT[u], order.begin() + outT[u]);
            std::sort(sub.begin(), sub.end());
            sub.erase(std::unique(sub.begin(), sub.end()), sub.end());
            ans[i] = k > (int)sub.size() ? -1 : sub[k - 1];
        }
        return ans;
    }
};
