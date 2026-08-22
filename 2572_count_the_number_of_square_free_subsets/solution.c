// LeetCode 2572 - Count the Number of Square-Free Subsets
// https://leetcode.com/problems/count-the-number-of-square-free-subsets/

#include <stdlib.h>
#include <string.h>

int squareFreeSubsets(int* nums, int numsSize) {
    const int MOD = 1000000007;
    int primes[10] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
    int freq[31];
    memset(freq, 0, sizeof(freq));
    for (int i = 0; i < numsSize; i++) freq[nums[i]]++;
    int* dp = (int*)calloc(1 << 10, sizeof(int));
    dp[0] = 1;
    for (int x = 2; x <= 30; x++) {
        if (freq[x] == 0) continue;
        int mask = 0, xx = x, bad = 0;
        for (int i = 0; i < 10; i++) {
            int cnt = 0;
            while (xx % primes[i] == 0) { xx /= primes[i]; cnt++; if (cnt > 1) { bad = 1; break; } }
            if (bad) break;
            if (cnt == 1) mask |= 1 << i;
        }
        if (bad) continue;
        for (int state = (1 << 10) - 1; state >= 0; state--) {
            if ((state & mask) == 0) {
                dp[state | mask] = (int)(((long long)dp[state | mask] + (long long)dp[state] * freq[x]) % MOD);
            }
        }
    }
    int ans = 0;
    for (int i = 0; i < (1 << 10); i++) ans = (ans + dp[i]) % MOD;
    int mul = 1;
    for (int i = 0; i < freq[1]; i++) mul = mul * 2 % MOD;
    ans = (int)((long long)ans * mul % MOD);
    ans = (ans - 1 + MOD) % MOD;
    free(dp);
    return ans;
}
