// LeetCode 3315 - Construct the Minimum Bitwise Array II
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

#include <stdlib.h>

int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        int n = nums[i];
        ans[i] = -1;
        if (n == 2) continue;
        for (int b = 0; b < 31; b++) {
            if (((n >> b) & 1) == 0) continue;
            int x = n ^ (1 << b);
            if ((x | (x + 1)) == n) { ans[i] = x; break; }
        }
    }
    *returnSize = numsSize;
    return ans;
}
