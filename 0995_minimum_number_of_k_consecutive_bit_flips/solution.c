// LeetCode 0995 - Minimum Number of K Consecutive Bit Flips
// https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

#include <stdlib.h>

int minKBitFlips(int* nums, int numsSize, int k) {
    int* flip = (int*)calloc((size_t)numsSize, sizeof(int));
    int ans = 0, flipped = 0;
    for (int i = 0; i < numsSize; i++) {
        if (i >= k) flipped ^= flip[i - k];
        if (nums[i] == flipped) {
            if (i + k > numsSize) { free(flip); return -1; }
            ans++;
            flipped ^= 1;
            flip[i] = 1;
        }
    }
    free(flip);
    return ans;
}
