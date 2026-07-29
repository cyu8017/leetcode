// LeetCode 0976 - Largest Perimeter Triangle
// https://leetcode.com/problems/largest-perimeter-triangle/

#include <stdlib.h>

static int cmpDesc(const void* a, const void* b) { return *(const int*)b - *(const int*)a; }

int largestPerimeter(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpDesc);
    for (int i = 0; i + 2 < numsSize; i++) {
        if (nums[i] < nums[i + 1] + nums[i + 2])
            return nums[i] + nums[i + 1] + nums[i + 2];
    }
    return 0;
}
