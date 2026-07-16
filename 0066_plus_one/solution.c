// LeetCode 0066 - Plus One
// https://leetcode.com/problems/plus-one/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    for (int i = digitsSize - 1; i >= 0; i--) {
        if (digits[i] < 9) {
            digits[i]++;
            *returnSize = digitsSize;
            return digits;
        }
        digits[i] = 0;
    }

    int* result = (int*)malloc((size_t)(digitsSize + 1) * sizeof(int));
    result[0] = 1;
    for (int i = 0; i < digitsSize; i++) {
        result[i + 1] = 0;
    }
    *returnSize = digitsSize + 1;
    return result;
}
