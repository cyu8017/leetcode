// LeetCode 2827 - Number of Beautiful Integers in the Range
// https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

#include <cstring>
#include <string>

class Solution {
public:
    int numberOfBeautifulIntegers(int low, int high, int k) {
        auto count = [&](int n) {
            if (n < 0) return 0;
            std::string s = std::to_string(n);
            int memo[12][45][22][2][2];
            std::memset(memo, -1, sizeof(memo));
            auto dfs = [&](auto&& self, int pos, int diff, int mod, int tight, int started) -> int {
                if (pos == (int)s.size()) return started && diff == 0 && mod == 0;
                int& res = memo[pos][diff + 20][mod][tight][started];
                if (res != -1) return res;
                int up = tight ? s[pos] - '0' : 9;
                int ans = 0;
                for (int d = 0; d <= up; d++) {
                    int nt = tight && d == up;
                    if (!started) {
                        if (d == 0) ans += self(self, pos + 1, diff, mod, nt, 0);
                        else {
                            int nd = diff + (d % 2 == 0 ? 1 : -1);
                            ans += self(self, pos + 1, nd, d % k, nt, 1);
                        }
                    } else {
                        int nd = diff + (d % 2 == 0 ? 1 : -1);
                        ans += self(self, pos + 1, nd, (mod * 10 + d) % k, nt, 1);
                    }
                }
                return res = ans;
            };
            return dfs(dfs, 0, 0, 0, 1, 0);
        };
        return count(high) - count(low - 1);
    }
};
