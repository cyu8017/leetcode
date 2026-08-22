// LeetCode 2740 - Find the Value of the Partition
// https://leetcode.com/problems/find-the-value-of-the-partition/

#include <stdlib.h>

static int cmp2740(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int findValueOfPartition(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp2740);
    int ans = nums[1] - nums[0];
    for (int i = 2; i < numsSize; i++) {
        int d = nums[i] - nums[i - 1];
        if (d < ans) ans = d;
    }
    return ans;
}
