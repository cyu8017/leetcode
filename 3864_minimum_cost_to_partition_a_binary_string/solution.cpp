// LeetCode 3864 - Minimum Cost To Partition A Binary String
// https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/

#include <algorithm>
#include <cstdint>
#include <functional>
#include <string>
#include <vector>

class Solution {
public:
    long long minCost(std::string s, int encCost, int flatCost) {
        int n = (int)s.size();
        std::vector<int> pre(n + 1, 0);
        for (int i = 1; i <= n; i++) pre[i] = pre[i - 1] + (s[i - 1] - '0');
        std::function<int64_t(int, int)> dfs = [&](int l, int r) {
            int x = pre[r] - pre[l];
            int64_t res = x != 0 ? (int64_t)(r - l) * x * encCost : flatCost;
            if ((r - l) % 2 == 0) {
                int m = (l + r) / 2;
                res = std::min(res, dfs(l, m) + dfs(m, r));
            }
            return res;
        };
        return dfs(0, n);
    }
};
