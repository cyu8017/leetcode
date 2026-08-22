// LeetCode 3194 - Minimum Average of Smallest and Largest Elements
// https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

#include <stdlib.h>

static int cmp3194(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

double minimumAverage(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), cmp3194);
    int ans = 1 << 30;
    for (int i = 0; i < numsSize / 2; i++) {
        int v = nums[i] + nums[numsSize - i - 1];
        if (v < ans) ans = v;
    }
    return ans / 2.0;
}
