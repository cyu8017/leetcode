// LeetCode 3254 - Find the Power of K-Size Subarrays I
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

#include <stdlib.h>

int* resultsArray(int* nums, int numsSize, int k, int* returnSize) {
    int m = numsSize - k + 1;
    int* ans = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) {
        int ok = 1;
        for (int j = i + 1; j < i + k; j++) {
            if (nums[j] != nums[j - 1] + 1) { ok = 0; break; }
        }
        ans[i] = ok ? nums[i + k - 1] : -1;
    }
    *returnSize = m;
    return ans;
}
