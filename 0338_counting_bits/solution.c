// LeetCode 0338 - Counting Bits
// https://leetcode.com/problems/counting-bits/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize) {
    *returnSize = n + 1;
    int* result = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int index = 1; index <= n; index++) {
        result[index] = result[index & (index - 1)] + 1;
    }
    return result;
}
