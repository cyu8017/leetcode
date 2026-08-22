// LeetCode 2598 - Smallest Missing Non-negative Integer After Operations
// https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

#include <stdlib.h>
#include <string.h>

int findSmallestInteger(int* nums, int numsSize, int value) {
    int* cnt = (int*)calloc((size_t)value, sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        int r = nums[i] % value;
        if (r < 0) r += value;
        cnt[r]++;
    }
    int mex = 0;
    while (cnt[mex % value] > 0) {
        cnt[mex % value]--;
        mex++;
    }
    free(cnt);
    return mex;
}
