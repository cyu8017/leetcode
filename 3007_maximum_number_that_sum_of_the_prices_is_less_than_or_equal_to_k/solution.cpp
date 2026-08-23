// LeetCode 3007 - Maximum Number That Sum of the Prices Is Less Than or Equal to K
// https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

#include <cstring>

class Solution {
public:
    long long findMaximumNumber(long long k, int x) {
        long long l = 1, r = (long long)1e17;
        long long num = 0;
        long long f[65][65];
        auto dfs = [&](auto&& self, int pos, int cnt, bool limit) -> long long {
            if (pos == 0) return cnt;
            if (!limit && f[pos][cnt] != -1) return f[pos][cnt];
            long long ans = 0;
            int up = limit ? (int)((num >> (pos - 1)) & 1) : 1;
            for (int i = 0; i <= up; i++) {
                int v = cnt;
                if (i == 1 && pos % x == 0) v++;
                ans += self(self, pos - 1, v, limit && i == up);
            }
            if (!limit) f[pos][cnt] = ans;
            return ans;
        };
        while (l < r) {
            long long mid = (l + r + 1) >> 1;
            num = mid;
            int m = num == 0 ? 0 : 64 - __builtin_clzll((unsigned long long)num);
            std::memset(f, -1, sizeof(f));
            if (dfs(dfs, m, 0, true) <= k) l = mid;
            else r = mid - 1;
        }
        return l;
    }
};
