// LeetCode 2183 - Count Array Pairs Divisible by K
// https://leetcode.com/problems/count-array-pairs-divisible-by-k/

#include <stdlib.h>

static int gcd2183(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

long long countPairs(int* nums, int numsSize, int k) {
    int* freq = (int*)calloc((size_t)k + 1, sizeof(int));
    int* keys = (int*)malloc((size_t)(k + 1) * sizeof(int));
    int kn = 0;
    long long ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int g1 = gcd2183(nums[i], k);
        for (int t = 0; t < kn; t++) {
            int g2 = keys[t];
            if ((long long)g1 * g2 % k == 0) ans += freq[g2];
        }
        if (freq[g1] == 0) keys[kn++] = g1;
        freq[g1]++;
    }
    free(freq); free(keys);
    return ans;
}
