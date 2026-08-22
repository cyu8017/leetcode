// LeetCode 2411 - Smallest Subarrays With Maximum Bitwise OR
// https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

#include <stdlib.h>

int* smallestSubarrays(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    int last[32];
    for (int i = 0; i < 32; i++) last[i] = -1;
    for (int i = numsSize - 1; i >= 0; i--) {
        for (int b = 0; b < 32; b++) if ((nums[i] >> b) & 1) last[b] = i;
        int far = i;
        for (int b = 0; b < 32; b++) if (last[b] > far) far = last[b];
        ans[i] = far - i + 1;
    }
    *returnSize = numsSize;
    return ans;
}
