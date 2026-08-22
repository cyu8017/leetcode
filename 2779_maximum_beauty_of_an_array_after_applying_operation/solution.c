// LeetCode 2779 - Maximum Beauty of an Array After Applying Operation
// https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int maximumBeauty(int* nums, int numsSize, int k) {
    qsort(nums, numsSize, sizeof(int), cmp_int);
    int ans = 0, left = 0;
    for (int right = 0; right < numsSize; right++) {
        while (nums[right] - nums[left] > 2 * k) left++;
        if (right - left + 1 > ans) ans = right - left + 1;
    }
    return ans;
}
