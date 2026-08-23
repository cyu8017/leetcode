// LeetCode 3385 - Minimum Time to Break Locks II
// https://leetcode.com/problems/minimum-time-to-break-locks-ii/

#include <cstdint>
#include <vector>

class Solution {
    static int bitsOnes(int x) {
        int c = 0;
        while (x > 0) {
            c += x & 1;
            x >>= 1;
        }
        return c;
    }

public:
    int findMinimumTime(std::vector<int>& strength) {
        int n = (int)strength.size();
        int N = 1 << n;
        const long long inf = (long long)1e18;
        std::vector<long long> dp(N, inf);
        dp[0] = 0;
        int k = 1;
        for (int mask = 0; mask < N; mask++) {
            if (dp[mask] == inf) continue;
            int opened = bitsOnes(mask);
            int x = 1 + opened * k;
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) continue;
                int t = (strength[i] + x - 1) / x;
                int nmask = mask | (1 << i);
                if (dp[mask] + t < dp[nmask]) dp[nmask] = dp[mask] + t;
            }
        }
        return (int)dp[N - 1];
    }
};
