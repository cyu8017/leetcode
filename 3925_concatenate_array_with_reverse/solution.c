// LeetCode 3925 - Concatenate Array With Reverse
// https://leetcode.com/problems/concatenate-array-with-reverse/

#include <stdlib.h>

int* concatWithReverse(int* nums, int numsSize, int* returnSize) {
    int n = numsSize;
    int* ans = malloc((size_t)(2 * n) * sizeof(int));
    for (int i = 0; i < n; i++) {
        ans[i] = nums[i];
        ans[i + n] = nums[n - i - 1];
    }
    *returnSize = 2 * n;
    return ans;
}
