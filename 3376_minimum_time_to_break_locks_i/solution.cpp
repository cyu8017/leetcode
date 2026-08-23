// LeetCode 3376 - Minimum Time to Break Locks I
// https://leetcode.com/problems/minimum-time-to-break-locks-i/

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
    int findMinimumTime(std::vector<int>& strength, int k) {
        int n = (int)strength.size();
        const int inf = 1000000000;
        int N = 1 << n;
        std::vector<int> dp(N, inf);
        dp[0] = 0;
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
        return dp[N - 1];
    }
};
