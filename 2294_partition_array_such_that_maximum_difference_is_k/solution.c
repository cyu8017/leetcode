// LeetCode 2294 - Partition Array Such That Maximum Difference Is K
// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int partitionArray(int* nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    int ans = 1;
    int start = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] - start > k) {
            ans++;
            start = nums[i];
        }
    }
    return ans;
}
