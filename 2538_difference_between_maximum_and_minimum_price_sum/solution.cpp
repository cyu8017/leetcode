// LeetCode 2538 - Difference Between Maximum and Minimum Price Sum
// https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

#include <functional>
#include <vector>

class Solution {
public:
    long long maxOutput(int n, std::vector<std::vector<int>>& edges, std::vector<int>& price) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        long long ans = 0;
        std::function<long long(int, int)> dfs = [&](int u, int p) {
            long long maxChild = 0;
            for (int v : g[u]) {
                if (v == p) continue;
                long long child = dfs(v, u);
                if (child > maxChild) maxChild = child;
                if (child > ans) ans = child;
            }
            return (long long)price[u] + maxChild;
        };
        dfs(0, -1);
        return ans;
    }
};
