// LeetCode 3621 - Number of Integers With Popcount Depth Equal to K I
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/

#include <map>
#include <string>
#include <tuple>

class Solution {
public:
    long long popcountDepth(long long n, int k) {
        if (k == 0) return n >= 1 ? 1 : 0;
        auto depth = [](int x) {
            if (x <= 0) return 100;
            int d = 0;
            while (x > 1) {
                x = __builtin_popcount((unsigned)x);
                d++;
            }
            return d;
        };
        std::string s;
        for (long long x = n; x > 0; x >>= 1) s = char('0' + (x & 1)) + s;
        if (s.empty()) s = "0";
        std::map<std::tuple<int, int, int, int>, long long> memo;
        auto dfs = [&](auto&& self, int pos, int tight, int started, int pc) -> long long {
            if (pos == (int)s.size()) {
                if (!started) return 0;
                if (pc == 1) return k == 1 ? 1 : 0;
                return depth(pc) == k - 1 ? 1 : 0;
            }
            auto key = std::make_tuple(pos, tight, started, pc);
            if (memo.count(key)) return memo[key];
            int up = tight ? s[pos] - '0' : 1;
            long long res = 0;
            for (int dig = 0; dig <= up; dig++) {
                int nt = (tight && dig == up) ? 1 : 0;
                if (!started && dig == 0) res += self(self, pos + 1, nt, 0, 0);
                else res += self(self, pos + 1, nt, 1, pc + dig);
            }
            return memo[key] = res;
        };
        return dfs(dfs, 0, 1, 0, 0);
    }
};
