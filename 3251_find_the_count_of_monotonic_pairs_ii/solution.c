// LeetCode 3251 - Find the Count of Monotonic Pairs II
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/

#include <stdlib.h>
#include <string.h>

int countOfPairs(int* nums, int numsSize) {
    const int mod = 1000000007;
    int maxV = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > maxV) maxV = nums[i];
    int* dp = (int*)calloc((size_t)(maxV + 1), sizeof(int));
    for (int a = 0; a <= nums[0]; a++) dp[a] = 1;
    for (int i = 1; i < numsSize; i++) {
        int* ndp = (int*)calloc((size_t)(maxV + 1), sizeof(int));
        int* pref = (int*)calloc((size_t)(maxV + 2), sizeof(int));
        for (int a = 0; a <= maxV; a++) pref[a + 1] = (pref[a] + dp[a]) % mod;
        for (int a2 = 0; a2 <= nums[i]; a2++) {
            int b2 = nums[i] - a2;
            int maxA1 = a2;
            int lim = nums[i - 1] - b2;
            if (lim < maxA1) maxA1 = lim;
            if (maxA1 < 0) continue;
            if (maxA1 > maxV) maxA1 = maxV;
            ndp[a2] = pref[maxA1 + 1];
        }
        free(dp); free(pref);
        dp = ndp;
    }
    int ans = 0;
    for (int i = 0; i <= maxV; i++) ans = (ans + dp[i]) % mod;
    free(dp);
    return ans;
}
