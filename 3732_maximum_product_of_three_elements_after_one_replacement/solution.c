// LeetCode 3732 - Maximum Product of Three Elements After One Replacement
// https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}
static long long llmax(long long a, long long b) { return a > b ? a : b; }

long long maxProduct(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    int n = numsSize;
    long long a = nums[0], b = nums[1], c = nums[n - 2], d = nums[n - 1];
    const long long x = 100000;
    return llmax(a * b * x, llmax(c * d * x, -a * d * x));
}
