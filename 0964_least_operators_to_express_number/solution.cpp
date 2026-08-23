// LeetCode 0964 - Least Operators to Express Number
// https://leetcode.com/problems/least-operators-to-express-number/

#include <algorithm>
#include <unordered_map>

class Solution {
public:
    int leastOpsExpressTarget(int x, int target) {
        std::unordered_map<int, int> memo;
        auto dfs = [&](auto&& self, int t) -> int {
            if (memo.count(t)) return memo[t];
            if (x > t) return memo[t] = std::min(2 * t - 1, 2 * (x - t));
            if (x == t) return memo[t] = 0;
            long long prod = x;
            int n = 0;
            while (prod < t) {
                prod *= x;
                n++;
            }
            if (prod == t) return memo[t] = n;
            int ans = self(self, t - (int)(prod / x)) + n;
            if (prod < 2LL * t) ans = std::min(ans, self(self, (int)prod - t) + n + 1);
            return memo[t] = ans;
        };
        return dfs(dfs, target);
    }
};
