// LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
// https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

#include <stdlib.h>
#include <string.h>

static int squareFree(int x) {
    int res = 1;
    for (int p = 2; p * p <= x; p++) {
        int cnt = 0;
        while (x % p == 0) { x /= p; cnt++; }
        if (cnt % 2 == 1) res *= p;
    }
    if (x > 1) res *= x;
    return res;
}

long long maximumSum(int* nums, int numsSize) {
    long long* groups = (long long*)calloc(numsSize + 1, sizeof(long long));
    long long ans = 0;
    for (int i = 1; i <= numsSize; i++) {
        int sf = squareFree(i);
        groups[sf] += nums[i - 1];
        if (groups[sf] > ans) ans = groups[sf];
    }
    free(groups);
    return ans;
}
