// LeetCode 3250 - Find the Count of Monotonic Pairs I
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/

#include <string.h>

int countOfPairs(int* nums, int numsSize) {
    const int mod = 1000000007;
    int dp[51];
    memset(dp, 0, sizeof(dp));
    for (int a = 0; a <= nums[0]; a++) dp[a] = 1;
    for (int i = 1; i < numsSize; i++) {
        int ndp[51];
        memset(ndp, 0, sizeof(ndp));
        int pref[52];
        pref[0] = 0;
        for (int a = 0; a <= 50; a++) pref[a + 1] = (pref[a] + dp[a]) % mod;
        for (int a2 = 0; a2 <= nums[i]; a2++) {
            int b2 = nums[i] - a2;
            int maxA1 = a2;
            int lim = nums[i - 1] - b2;
            if (lim < maxA1) maxA1 = lim;
            if (maxA1 < 0) continue;
            if (maxA1 > 50) maxA1 = 50;
            ndp[a2] = pref[maxA1 + 1];
        }
        memcpy(dp, ndp, sizeof(dp));
    }
    int ans = 0;
    for (int i = 0; i <= 50; i++) ans = (ans + dp[i]) % mod;
    return ans;
}
