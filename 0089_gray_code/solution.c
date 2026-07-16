// LeetCode 0089 - Gray Code
// https://leetcode.com/problems/gray-code/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* grayCode(int n, int* returnSize) {
    int size = 1 << n;
    int* result = (int*)malloc((size_t)size * sizeof(int));
    for (int i = 0; i < size; i++) {
        result[i] = i ^ (i >> 1);
    }
    *returnSize = size;
    return result;
}
