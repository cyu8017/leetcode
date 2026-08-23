// LeetCode 3791 - Number Of Balanced Integers In A Range
// https://leetcode.com/problems/number-of-balanced-integers-in-a-range/

#include <cstdint>
#include <cstring>
#include <string>

class Solution {
    static constexpr int BASE = 90;
    std::string num;
    int64_t f[20][181];

    int64_t dfs(int pos, int diff, bool lim) {
        if (pos >= (int)num.size()) return diff == 0 ? 1 : 0;
        if (!lim && f[pos][diff + BASE] != -1) return f[pos][diff + BASE];
        int up = lim ? num[pos] - '0' : 9;
        int64_t res = 0;
        for (int i = 0; i <= up; i++) {
            if (pos % 2 == 0) res += dfs(pos + 1, diff + i, lim && i == up);
            else res += dfs(pos + 1, diff - i, lim && i == up);
        }
        if (!lim) f[pos][diff + BASE] = res;
        return res;
    }

public:
    long long countBalanced(long long low, long long high) {
        if (high < 11) return 0;
        if (low < 11) low = 11;
        num = std::to_string(low - 1);
        std::memset(f, -1, sizeof(f));
        int64_t a = dfs(0, 0, true);
        num = std::to_string(high);
        std::memset(f, -1, sizeof(f));
        int64_t b = dfs(0, 0, true);
        return b - a;
    }
};
