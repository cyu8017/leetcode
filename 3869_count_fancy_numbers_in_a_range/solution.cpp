// LeetCode 3869 - Count Fancy Numbers In A Range
// https://leetcode.com/problems/count-fancy-numbers-in-a-range/

#include <cstdint>
#include <functional>
#include <string>
#include <vector>

class Solution {
    static bool check(int s) {
        if (s < 100) return s % 11 != 0;
        int mid = (s / 10) % 10;
        int last = s % 10;
        return mid > 1 && mid < last;
    }

public:
    long long countFancy(long long l, long long r) {
        auto calc = [&](int64_t x) {
            std::string num = std::to_string(x);
            int n = (int)num.size();
            std::vector f(n, std::vector(9 * n + 1, std::vector(10, std::vector<int64_t>(4, -1))));
            std::function<int64_t(int, int, int, int, bool)> dfs =
                [&](int pos, int s, int prev, int st, bool lim) -> int64_t {
                if (pos >= n) {
                    if (st != 3) return 1;
                    return check(s) ? 1 : 0;
                }
                if (!lim && f[pos][s][prev][st] != -1) return f[pos][s][prev][st];
                int up = lim ? num[pos] - '0' : 9;
                int64_t res = 0;
                for (int i = 0; i <= up; i++) {
                    int nxtSt = st;
                    if (st == 0) {
                        if (prev == 0) nxtSt = 0;
                        else if (i > prev) nxtSt = 1;
                        else if (i < prev) nxtSt = 2;
                        else nxtSt = 3;
                    } else if (st == 1) {
                        nxtSt = i > prev ? 1 : 3;
                    } else if (st == 2) {
                        nxtSt = i < prev ? 2 : 3;
                    } else {
                        nxtSt = 3;
                    }
                    res += dfs(pos + 1, s + i, i, nxtSt, lim && i == up);
                }
                if (!lim) f[pos][s][prev][st] = res;
                return res;
            };
            return dfs(0, 0, 0, 0, true);
        };
        return calc(r) - calc(l - 1);
    }
};
