// LeetCode 1877 - Minimize Maximum Pair Sum in Array
// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

#include <stdlib.h>

static int cmpAsc(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int minPairSum(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpAsc);
    int best = 0;
    for (int i = 0; i < numsSize / 2; i++) {
        int sum = nums[i] + nums[numsSize - 1 - i];
        if (sum > best) best = sum;
    }
    return best;
}
