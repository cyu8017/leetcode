// LeetCode 0891 - Sum of Subsequence Widths
// https://leetcode.com/problems/sum-of-subsequence-widths/

#include <stdlib.h>

#define MOD 1000000007

static int cmp_int(const void* a, const void* b) {
    return (*(const int*)a) - (*(const int*)b);
}

int sumSubseqWidths(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    int n = numsSize;
    long long* pow2 = (long long*)malloc((size_t)n * sizeof(long long));
    pow2[0] = 1;
    for (int i = 1; i < n; i++) pow2[i] = (pow2[i - 1] * 2) % MOD;
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        ans = (ans + nums[i] * ((pow2[i] - pow2[n - 1 - i] + MOD) % MOD)) % MOD;
    }
    free(pow2);
    return (int)ans;
}
