// LeetCode 3727 - Maximum Alternating Sum of Squares
// https://leetcode.com/problems/maximum-alternating-sum-of-squares/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

long long maxAlternatingSum(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; i++) nums[i] *= nums[i];
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    int m = numsSize / 2;
    long long ans = 0;
    for (int i = 0; i < m; i++) ans -= nums[i];
    for (int i = m; i < numsSize; i++) ans += nums[i];
    return ans;
}
