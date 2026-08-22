// LeetCode 3289 - The Two Sneaky Numbers of Digitville
// https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

#include <stdlib.h>
#include <stdbool.h>

int* getSneakyNumbers(int* nums, int numsSize, int* returnSize) {
    bool* seen = (bool*)calloc(101, sizeof(bool));
    int* ans = (int*)malloc(2 * sizeof(int));
    int n = 0;
    for (int i = 0; i < numsSize; i++) {
        if (seen[nums[i]]) ans[n++] = nums[i];
        else seen[nums[i]] = true;
    }
    free(seen);
    *returnSize = n;
    return ans;
}
