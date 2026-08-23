// LeetCode 3802 - Number of Ways to Paint Sheets
// https://leetcode.com/problems/number-of-ways-to-paint-sheets/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
public:
    int numberOfWays(int n, std::vector<int>& limit) {
        const int64_t MOD = 1000000007;
        std::sort(limit.begin(), limit.end());
        std::vector<int> points = {1, n};
        for (int x : limit) {
            if (x + 1 > 1 && x + 1 < n) points.push_back(x + 1);
            if (n - x > 1 && n - x < n) points.push_back(n - x);
        }
        std::sort(points.begin(), points.end());
        points.erase(std::unique(points.begin(), points.end()), points.end());
        auto countGE = [&](int x) -> int64_t {
            return (int64_t)(limit.end() - std::lower_bound(limit.begin(), limit.end(), x));
        };
        int64_t ans = 0;
        for (int i = 0; i + 1 < (int)points.size(); i++) {
            int x = points[i];
            int64_t a = countGE(x), b = countGE(n - x);
            int64_t same = countGE(std::max(x, n - x));
            int64_t ways = (a * b - same) % MOD;
            int64_t length = points[i + 1] - x;
            ans = (ans + ways * length) % MOD;
        }
        if (ans < 0) ans += MOD;
        return (int)ans;
    }
};
