// LeetCode 3757 - Number of Effective Subsequences
// https://leetcode.com/problems/number-of-effective-subsequences/

#include <stdlib.h>

static int bitCount(int x) {
    int res = 0;
    while (x) { x &= x - 1; res++; }
    return res;
}

int countEffectiveSubsequences(int* nums, int numsSize) {
    const int mod = 1000000007;
    int all = 0;
    for (int i = 0; i < numsSize; i++) all |= nums[i];
    int bits[20], m = 0;
    for (int b = 0; b < 20; b++) if ((all >> b) & 1) bits[m++] = b;
    int sz = 1 << m;
    int* freq = (int*)calloc((size_t)sz, sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        int mask = 0;
        for (int j = 0; j < m; j++) if ((nums[i] >> bits[j]) & 1) mask |= 1 << j;
        freq[mask]++;
    }
    int* disjoint = (int*)malloc((size_t)sz * sizeof(int));
    for (int i = 0; i < sz; i++) disjoint[i] = freq[i];
    for (int b = 0; b < m; b++) {
        for (int mask = 0; mask < sz; mask++) {
            if ((mask >> b) & 1) disjoint[mask] += disjoint[mask ^ (1 << b)];
        }
    }
    int* pow2 = (int*)malloc((size_t)(numsSize + 1) * sizeof(int));
    pow2[0] = 1;
    for (int i = 1; i <= numsSize; i++) pow2[i] = pow2[i - 1] * 2 % mod;
    int ans = 0, full = sz - 1;
    for (int s = 1; s <= full; s++) {
        int ways = pow2[disjoint[full ^ s]];
        if (bitCount(s) & 1) { ans += ways; if (ans >= mod) ans -= mod; }
        else { ans -= ways; if (ans < 0) ans += mod; }
    }
    free(freq); free(disjoint); free(pow2);
    return ans;
}
