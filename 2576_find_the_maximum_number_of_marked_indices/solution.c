// LeetCode 2576 - Find the Maximum Number of Marked Indices
// https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int maxNumOfMarkedIndices(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    int i = 0, ans = 0;
    for (int j = (numsSize + 1) / 2; j < numsSize; j++) {
        if (2 * nums[i] <= nums[j]) { ans += 2; i++; }
    }
    return ans;
}
