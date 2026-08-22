// LeetCode 2625 - Flatten Deeply Nested Array
// https://leetcode.com/problems/flatten-deeply-nested-array/

#include <stdlib.h>

// JavaScript nested-array problem; C stand-in flattens a 1D int array (already flat).
int* flat(int* arr, int arrSize, int n, int* returnSize) {
    (void)n;
    int* out = (int*)malloc((size_t)arrSize * sizeof(int));
    for (int i = 0; i < arrSize; i++) out[i] = arr[i];
    *returnSize = arrSize;
    return out;
}
