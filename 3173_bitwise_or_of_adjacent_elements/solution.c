// LeetCode 3173 - Bitwise OR of Adjacent Elements
// https://leetcode.com/problems/bitwise-or-of-adjacent-elements/

#include <stdlib.h>

int* orArray(int* nums, int numsSize, int* returnSize) {
    int* ans = malloc((numsSize - 1) * sizeof(int));
    for (int i = 0; i < numsSize - 1; i++) ans[i] = nums[i] | nums[i + 1];
    *returnSize = numsSize - 1;
    return ans;
}
