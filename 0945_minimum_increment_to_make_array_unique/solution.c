// LeetCode 0945 - Minimum Increment to Make Array Unique
// https://leetcode.com/problems/minimum-increment-to-make-array-unique/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int minIncrementForUnique(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    int ans = 0;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] <= nums[i - 1]) {
            int need = nums[i - 1] + 1;
            ans += need - nums[i];
            nums[i] = need;
        }
    }
    return ans;
}
