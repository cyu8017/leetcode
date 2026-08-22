// LeetCode 3255 - Find the Power of K-Size Subarrays II
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

#include <stdlib.h>
#include <string.h>

int* resultsArray(int* nums, int numsSize, int k, int* returnSize) {
    int m = numsSize - k + 1;
    int* ans = (int*)malloc((size_t)m * sizeof(int));
    if (k == 1) {
        memcpy(ans, nums, (size_t)numsSize * sizeof(int));
        *returnSize = m;
        return ans;
    }
    int streak = 1;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] == nums[i - 1] + 1) streak++;
        else streak = 1;
        if (i >= k - 1) ans[i - k + 1] = (streak >= k) ? nums[i] : -1;
    }
    *returnSize = m;
    return ans;
}
