// LeetCode 1994 - The Number of Good Subsets
// https://leetcode.com/problems/the-number-of-good-subsets/

#include <stdlib.h>

static long long modPow(long long a, long long e, long long mod) {
    long long r = 1;
    while (e) {
        if (e & 1) r = r * a % mod;
        a = a * a % mod;
        e >>= 1;
    }
    return r;
}

int numberOfGoodSubsets(int* nums, int numsSize) {
    const long long MOD = 1000000007LL;
    int primes[10] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
    int masks[31];
    for (int x = 0; x < 31; x++) masks[x] = 0;
    for (int x = 2; x <= 30; x++) {
        int m = 0, y = x, ok = 1;
        for (int i = 0; i < 10; i++) {
            int p = primes[i];
            if (y % p == 0) {
                if ((y / p) % p == 0) { ok = 0; break; }
                m |= 1 << i;
                y /= p;
            }
        }
        masks[x] = ok ? m : -1;
    }
    int cnt[31] = {0};
    for (int i = 0; i < numsSize; i++) cnt[nums[i]]++;
    int P = 1 << 10;
    long long* dp = (long long*)calloc((size_t)P, sizeof(long long));
    dp[0] = 1;
    for (int x = 2; x <= 30; x++) {
        if (cnt[x] == 0 || masks[x] < 0) continue;
        int m = masks[x];
        for (int state = P - 1; state >= 0; state--) {
            if (state & m) continue;
            dp[state | m] = (dp[state | m] + dp[state] * cnt[x]) % MOD;
        }
    }
    long long ans = 0;
    for (int i = 1; i < P; i++) ans = (ans + dp[i]) % MOD;
    ans = ans * modPow(2, cnt[1], MOD) % MOD;
    free(dp);
    return (int)ans;
}
