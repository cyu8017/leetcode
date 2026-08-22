// LeetCode 3704 - Count No-Zero Pairs That Sum to N
// https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/

#include <stdio.h>
#include <string.h>

long long countNoZeroPairs(long long n) {
    char s[32];
    sprintf(s, "%lld", n);
    int m = (int)strlen(s);
    int digits[32];
    for (int i = 0; i < m; i++) digits[i] = s[m - 1 - i] - '0';
    digits[m] = 0;
    long long dp[2][2][2];
    memset(dp, 0, sizeof(dp));
    dp[0][1][1] = 1;
    for (int pos = 0; pos < m + 1; pos++) {
        long long ndp[2][2][2];
        memset(ndp, 0, sizeof(ndp));
        int target = digits[pos];
        for (int carry = 0; carry <= 1; carry++) {
            for (int aliveA = 0; aliveA <= 1; aliveA++) {
                for (int aliveB = 0; aliveB <= 1; aliveB++) {
                    long long ways = dp[carry][aliveA][aliveB];
                    if (!ways) continue;
                    int A[10][2], aLen = 0;
                    if (aliveA == 1) {
                        for (int d = 1; d <= 9; d++) { A[aLen][0] = d; A[aLen][1] = 1; aLen++; }
                        if (pos > 0) { A[aLen][0] = 0; A[aLen][1] = 0; aLen++; }
                    } else { A[0][0] = 0; A[0][1] = 0; aLen = 1; }
                    int B[10][2], bLen = 0;
                    if (aliveB == 1) {
                        for (int d = 1; d <= 9; d++) { B[bLen][0] = d; B[bLen][1] = 1; bLen++; }
                        if (pos > 0) { B[bLen][0] = 0; B[bLen][1] = 0; bLen++; }
                    } else { B[0][0] = 0; B[0][1] = 0; bLen = 1; }
                    for (int ai = 0; ai < aLen; ai++) {
                        int da = A[ai][0], na = A[ai][1];
                        for (int bi = 0; bi < bLen; bi++) {
                            int db = B[bi][0], nb = B[bi][1];
                            int sum = da + db + carry;
                            if (sum % 10 != target) continue;
                            int ncarry = sum / 10;
                            ndp[ncarry][na][nb] += ways;
                        }
                    }
                }
            }
        }
        memcpy(dp, ndp, sizeof(dp));
    }
    return dp[0][0][0];
}

long long countPairs(long long n) {
    return countNoZeroPairs(n);
}
