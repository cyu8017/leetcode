// LeetCode 1005 - Maximize Sum Of Array After K Negations
// https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int largestSumAfterKNegations(int* nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    for (int i = 0; i < numsSize && k > 0; i++) {
        if (nums[i] < 0) {
            nums[i] = -nums[i];
            k--;
        }
    }
    if (k % 2) {
        qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
        nums[0] = -nums[0];
    }
    int sum = 0;
    for (int i = 0; i < numsSize; i++) sum += nums[i];
    return sum;
}
