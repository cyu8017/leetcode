// LeetCode 3290 - Maximum Multiplication Score
// https://leetcode.com/problems/maximum-multiplication-score/

#include <limits.h>

long long maxScore(int* a, int aSize, int* b, int bSize) {
    (void)aSize;
    const long long NEG = LLONG_MIN / 4;
    long long dp[5] = {0, NEG, NEG, NEG, NEG};
    for (int i = 0; i < bSize; i++) {
        long long x = b[i];
        for (int k = 4; k >= 1; k--) {
            if (dp[k - 1] == NEG) continue;
            long long v = dp[k - 1] + (long long)a[k - 1] * x;
            if (v > dp[k]) dp[k] = v;
        }
    }
    return dp[4];
}
