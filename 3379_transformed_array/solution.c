// LeetCode 3379 - Transformed Array
// https://leetcode.com/problems/transformed-array/

#include <stdlib.h>

int* constructTransformedArray(int* nums, int numsSize, int* returnSize) {
    int n = numsSize;
    int* ans = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        int j = ((i + nums[i]) % n + n) % n;
        ans[i] = nums[j];
    }
    *returnSize = n;
    return ans;
}
