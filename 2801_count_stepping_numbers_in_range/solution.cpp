// LeetCode 2801 - Count Stepping Numbers in Range
// https://leetcode.com/problems/count-stepping-numbers-in-range/

#include <cstdlib>
#include <cstring>
#include <string>

class Solution {
public:
    int countSteppingNumbers(std::string low, std::string high) {
        const int MOD = 1000000007;
        auto countTo = [&](const std::string& s) {
            int memo[85][2][11][2];
            std::memset(memo, -1, sizeof(memo));
            auto dfs = [&](auto&& self, int pos, int tight, int last, int started) -> int {
                if (pos == (int)s.size()) return started;
                int& res = memo[pos][tight][last + 1][started];
                if (res != -1) return res;
                int up = tight ? s[pos] - '0' : 9;
                long long ans = 0;
                for (int d = 0; d <= up; d++) {
                    int nt = tight && d == up;
                    if (!started) {
                        if (d == 0) ans += self(self, pos + 1, nt, -1, 0);
                        else ans += self(self, pos + 1, nt, d, 1);
                    } else if (std::abs(d - last) == 1) {
                        ans += self(self, pos + 1, nt, d, 1);
                    }
                }
                return res = (int)(ans % MOD);
            };
            return dfs(dfs, 0, 1, -1, 0);
        };
        auto dec = [](std::string s) {
            int i = (int)s.size() - 1;
            while (i >= 0 && s[i] == '0') { s[i] = '9'; i--; }
            if (i >= 0) s[i]--;
            int j = 0;
            while (j < (int)s.size() - 1 && s[j] == '0') j++;
            return s.substr(j);
        };
        int ans = (countTo(high) - countTo(dec(low))) % MOD;
        if (ans < 0) ans += MOD;
        return ans;
    }
};
