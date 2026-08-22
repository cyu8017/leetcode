// LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
// https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

#include <stdlib.h>
#include <string.h>

int countSubMultisets(int* nums, int numsSize, int l, int r) {
    const int mod = 1000000007;
    int* freq = (int*)calloc(20001, sizeof(int));
    int total = 0, maxv = 0;
    for (int i = 0; i < numsSize; i++) {
        freq[nums[i]]++;
        total += nums[i];
        if (nums[i] > maxv) maxv = nums[i];
    }
    if (total < l) { free(freq); return 0; }
    if (r > total) r = total;
    int* dp = (int*)calloc(r + 1, sizeof(int));
    dp[0] = 1;
    int zeros = freq[0];
    freq[0] = 0;
    for (int v = 1; v <= maxv; v++) {
        int c = freq[v];
        if (!c) continue;
        int* ndp = (int*)calloc(r + 1, sizeof(int));
        for (int sum = 0; sum <= r; sum++) {
            if (!dp[sum]) continue;
            for (int k = 0; k <= c && sum + k * v <= r; k++) {
                ndp[sum + k * v] = (ndp[sum + k * v] + dp[sum]) % mod;
            }
        }
        free(dp); dp = ndp;
    }
    int ans = 0;
    for (int s = l; s <= r; s++) ans = (ans + dp[s]) % mod;
    ans = (int)((long long)ans * (zeros + 1) % mod);
    free(dp); free(freq);
    return ans;
}
