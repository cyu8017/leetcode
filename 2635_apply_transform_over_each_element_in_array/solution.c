// LeetCode 2635 - Apply Transform Over Each Element in Array
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

#include <stdlib.h>

typedef int (*MapFn)(int, int);

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* mapArray(int* arr, int arrSize, MapFn fn, int* returnSize) {
    int* out = (int*)malloc((size_t)arrSize * sizeof(int));
    for (int i = 0; i < arrSize; i++) out[i] = fn(arr[i], i);
    *returnSize = arrSize;
    return out;
}
