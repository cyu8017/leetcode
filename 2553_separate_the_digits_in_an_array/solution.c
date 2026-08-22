// LeetCode 2553 - Separate the Digits in an Array
// https://leetcode.com/problems/separate-the-digits-in-an-array/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* separateDigits(int* nums, int numsSize, int* returnSize) {
    int cap = numsSize * 10;
    int* ans = (int*)malloc((size_t)cap * sizeof(int));
    int len = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        int digits[16];
        int dlen = 0;
        while (x > 0) {
            digits[dlen++] = x % 10;
            x /= 10;
        }
        for (int j = dlen - 1; j >= 0; j--) ans[len++] = digits[j];
    }
    *returnSize = len;
    return ans;
}
