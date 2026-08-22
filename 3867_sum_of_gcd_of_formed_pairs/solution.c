// LeetCode 3867 - Sum Of Gcd Of Formed Pairs
// https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

#include <stdlib.h>

static int gcd(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}
static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

long long gcdSum(int* nums, int numsSize) {
    int n = numsSize;
    int* prefixGcd = (int*)malloc((size_t)n * sizeof(int));
    int mx = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] > mx) mx = nums[i];
        prefixGcd[i] = gcd(nums[i], mx);
    }
    qsort(prefixGcd, (size_t)n, sizeof(int), cmp_int);
    long long ans = 0;
    for (int i = 0; i < n / 2; i++) ans += gcd(prefixGcd[i], prefixGcd[n - i - 1]);
    free(prefixGcd);
    return ans;
}
