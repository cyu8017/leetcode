// LeetCode 2653 - Sliding Subarray Beauty
// https://leetcode.com/problems/sliding-subarray-beauty/

#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getSubarrayBeauty(int* nums, int numsSize, int k, int x, int* returnSize) {
    int freq[101];
    memset(freq, 0, sizeof(freq));
    *returnSize = numsSize - k + 1;
    int* ans = (int*)malloc((size_t)(*returnSize) * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        freq[nums[i] + 50]++;
        if (i >= k) freq[nums[i - k] + 50]--;
        if (i >= k - 1) {
            int need = x, val = 0;
            for (int j = 0; j < 50; j++) {
                need -= freq[j];
                if (need <= 0) { val = j - 50; break; }
            }
            ans[i - k + 1] = val;
        }
    }
    return ans;
}
