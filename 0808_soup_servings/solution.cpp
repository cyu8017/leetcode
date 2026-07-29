// LeetCode 0808 - Soup Servings
// https://leetcode.com/problems/soup-servings/

#include <functional>
#include <unordered_map>

class Solution {
public:
    double soupServings(int n) {
        if (n >= 4800) {
            return 1.0;
        }
        int units = (n + 24) / 25;
        std::unordered_map<long long, double> memo;
        std::function<double(int, int)> dp = [&](int a, int b) -> double {
            if (a <= 0 && b <= 0) {
                return 0.5;
            }
            if (a <= 0) {
                return 1.0;
            }
            if (b <= 0) {
                return 0.0;
            }
            long long key = (static_cast<long long>(a) << 16) | b;
            if (auto it = memo.find(key); it != memo.end()) {
                return it->second;
            }
            double val = 0.25 * (dp(a - 4, b) + dp(a - 3, b - 1) + dp(a - 2, b - 2) +
                                 dp(a - 1, b - 3));
            return memo[key] = val;
        };
        return dp(units, units);
    }
};
