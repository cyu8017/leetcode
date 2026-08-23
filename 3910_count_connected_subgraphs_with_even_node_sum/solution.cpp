// LeetCode 3910 - Count Connected Subgraphs With Even Node Sum
// https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

#include <functional>
#include <vector>

class Solution {
public:
    int evenSumSubgraphs(std::vector<int>& nums, std::vector<std::vector<int>>& edges) {
        int n = (int)nums.size();
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        int m = (1 << n) - 1;
        int ans = 0;
        int vis = 0;

        std::function<void(int)> dfs = [&](int u) {
            vis |= 1 << u;
            for (int v : g[u]) {
                if (((vis >> v) & 1) == 0) dfs(v);
            }
        };

        for (int sub = 1; sub <= m; sub++) {
            int s = 0;
            for (int i = 0; i < n; i++) {
                if ((sub >> i) & 1) s += nums[i];
            }
            if (s % 2 != 0) continue;
            vis = m ^ sub;
            int start = 31 - __builtin_clz(sub);
            dfs(start);
            if (vis == m) ans++;
        }
        return ans;
    }
};
