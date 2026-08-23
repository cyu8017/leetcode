// LeetCode 2322 - Minimum Score After Removals on a Tree
// https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

#include <vector>
#include <functional>
#include <algorithm>
#include <climits>

class Solution {
public:
    int minimumScore(std::vector<int>& nums, std::vector<std::vector<int>>& edges) {
        int n = (int)nums.size();
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) { g[e[0]].push_back(e[1]); g[e[1]].push_back(e[0]); }
        std::vector<int> xorv(n), inT(n), outT(n);
        int time = 0;
        std::function<void(int,int)> dfs = [&](int u, int p) {
            inT[u] = time++;
            xorv[u] = nums[u];
            for (int v : g[u]) if (v != p) { dfs(v, u); xorv[u] ^= xorv[v]; }
            outT[u] = time;
        };
        dfs(0, -1);
        auto isAncestor = [&](int a, int b) {
            return inT[a] <= inT[b] && outT[b] <= outT[a];
        };
        int total = xorv[0], ans = INT_MAX;
        for (int i = 1; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int a, b, c;
                if (isAncestor(i, j)) { a = xorv[j]; b = xorv[i] ^ xorv[j]; c = total ^ xorv[i]; }
                else if (isAncestor(j, i)) { a = xorv[i]; b = xorv[j] ^ xorv[i]; c = total ^ xorv[j]; }
                else { a = xorv[i]; b = xorv[j]; c = total ^ xorv[i] ^ xorv[j]; }
                ans = std::min(ans, std::max({a, b, c}) - std::min({a, b, c}));
            }
        }
        return ans;
    }
};
