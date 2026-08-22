// LeetCode 3314 - Construct the Minimum Bitwise Array I
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

#include <stdlib.h>

int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        ans[i] = -1;
        for (int x = 0; x < nums[i]; x++) {
            if ((x | (x + 1)) == nums[i]) { ans[i] = x; break; }
        }
    }
    *returnSize = numsSize;
    return ans;
}
