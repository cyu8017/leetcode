// LeetCode 1984 - Minimum Difference Between Highest and Lowest of K Scores
// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int minimumDifference(int* nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    int best = nums[k - 1] - nums[0];
    for (int i = 1; i + k - 1 < numsSize; i++) {
        int diff = nums[i + k - 1] - nums[i];
        if (diff < best) best = diff;
    }
    return best;
}
