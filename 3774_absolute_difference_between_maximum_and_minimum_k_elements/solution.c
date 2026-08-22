// LeetCode 3774 - Absolute Difference Between Maximum And Minimum K Elements
// https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int absDifference(int* nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    int ans = 0;
    for (int i = 0; i < k; i++) {
        ans += nums[numsSize - i - 1] - nums[i];
    }
    return ans;
}
