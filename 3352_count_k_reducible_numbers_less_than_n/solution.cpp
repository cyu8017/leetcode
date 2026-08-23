// LeetCode 3352 - Count K-Reducible Numbers Less Than N
// https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

#include <map>
#include <string>
#include <tuple>
#include <vector>

class Solution {
    static int bitsPop(int x) {
        int c = 0;
        while (x > 0) {
            c += x & 1;
            x >>= 1;
        }
        return c;
    }

public:
    int countKReducibleNumbers(std::string s, int k) {
        const int mod = 1000000007;
        std::vector<int> red(801);
        red[1] = 0;
        for (int i = 2; i <= 800; i++) red[i] = 1 + red[bitsPop(i)];
        int n = (int)s.size();
        std::map<std::tuple<int, int, int>, int> memo;
        auto dfs = [&](auto&& self, int pos, bool tight, int ones) -> int {
            if (pos == n) {
                if (ones == 0) return 0;
                return red[ones] <= k - 1 ? 1 : 0;
            }
            auto key = std::make_tuple(pos, tight ? 1 : 0, ones);
            if (memo.count(key)) return memo[key];
            int up = tight ? (s[pos] - '0') : 1;
            int ans = 0;
            for (int d = 0; d <= up; d++) {
                bool nt = tight && d == up;
                ans = (ans + self(self, pos + 1, nt, ones + d)) % mod;
            }
            return memo[key] = ans;
        };
        return dfs(dfs, 0, true, 0);
    }
};
