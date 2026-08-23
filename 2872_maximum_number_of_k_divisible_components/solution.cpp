// LeetCode 2872 - Maximum Number of K-Divisible Components
// https://leetcode.com/problems/maximum-number-of-k-divisible-components/

#include <functional>
#include <vector>

class Solution {
public:
    int maxKDivisibleComponents(int n, std::vector<std::vector<int>>& edges, std::vector<int>& values, int k) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        int ans = 0;
        std::function<int(int, int)> dfs = [&](int u, int p) {
            int sum = values[u] % k;
            for (int v : g[u]) {
                if (v == p) continue;
                sum = (sum + dfs(v, u)) % k;
            }
            if (sum == 0) ans++;
            return sum;
        };
        dfs(0, -1);
        return ans;
    }
};
