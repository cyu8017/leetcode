// LeetCode 3883 - Count Non Decreasing Arrays With Given Digit Sums
// https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

#include <stdlib.h>

int countNonDecreasingArrays(int* digitSum, int digitSumSize) {
    const int mod = 1000000007;
    static int* groups[51];
    static int gsz[51];
    static int ready = 0;
    if (!ready) {
        int caps[51] = {0};
        for (int s = 0; s <= 50; s++) { groups[s] = NULL; gsz[s] = 0; }
        for (int x = 0; x <= 5000; x++) {
            int s = 0;
            for (int y = x; y > 0; y /= 10) s += y % 10;
            if (gsz[s] == caps[s]) {
                caps[s] = caps[s] ? caps[s] * 2 : 8;
                groups[s] = realloc(groups[s], (size_t)caps[s] * sizeof(int));
            }
            groups[s][gsz[s]++] = x;
        }
        ready = 1;
    }
    int* prevVals = groups[digitSum[0]];
    int prevN = gsz[digitSum[0]];
    int* dp = calloc((size_t)prevN, sizeof(int));
    for (int i = 0; i < prevN; i++) dp[i] = 1;
    for (int pos = 1; pos < digitSumSize; pos++) {
        int* curVals = groups[digitSum[pos]];
        int curN = gsz[digitSum[pos]];
        int* next = calloc((size_t)curN, sizeof(int));
        int j = 0, prefix = 0;
        for (int i = 0; i < curN; i++) {
            int x = curVals[i];
            while (j < prevN && prevVals[j] <= x) {
                prefix += dp[j];
                if (prefix >= mod) prefix -= mod;
                j++;
            }
            next[i] = prefix;
        }
        free(dp);
        prevVals = curVals;
        prevN = curN;
        dp = next;
    }
    int ans = 0;
    for (int i = 0; i < prevN; i++) {
        ans += dp[i];
        if (ans >= mod) ans -= mod;
    }
    free(dp);
    return ans;
}
