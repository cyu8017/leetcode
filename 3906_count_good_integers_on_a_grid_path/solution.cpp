// LeetCode 3906 - Count Good Integers On A Grid Path
// https://leetcode.com/problems/count-good-integers-on-a-grid-path/

#include <array>
#include <string>
#include <vector>

class Solution {
public:
    long long countGoodIntegersOnPath(long long l, long long r, std::string directions) {
        std::array<bool, 16> key{};
        int row = 0, col = 0;
        key[0] = true;
        for (char c : directions) {
            if (c == 'D') row++;
            else col++;
            key[row * 4 + col] = true;
        }

        std::string s;
        std::array<std::array<long long, 10>, 16> f{};

        auto dfs = [&](auto&& self, int pos, int last, bool lim) -> long long {
            if (pos == 16) return 1;
            if (!lim && f[pos][last] != -1) return f[pos][last];
            long long res = 0;
            int start = key[pos] ? last : 0;
            int end = lim ? (s[pos] - '0') : 9;
            for (int i = start; i <= end; i++) {
                int nextLast = key[pos] ? i : last;
                res += self(self, pos + 1, nextLast, lim && (i == end));
            }
            if (!lim) f[pos][last] = res;
            return res;
        };

        auto calc = [&](long long x) -> long long {
            if (x < 0) return 0;
            std::string t = std::to_string(x);
            s = std::string(16 - (int)t.size(), '0') + t;
            for (int i = 0; i < 16; i++) {
                for (int j = 0; j < 10; j++) f[i][j] = -1;
            }
            return dfs(dfs, 0, 0, true);
        };

        return calc(r) - calc(l - 1);
    }
};
