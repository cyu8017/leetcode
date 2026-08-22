// LeetCode 2634 - Filter Elements from Array
// https://leetcode.com/problems/filter-elements-from-array/

#include <stdlib.h>
#include <stdbool.h>

typedef bool (*FilterFn)(int, int);

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* filter(int* arr, int arrSize, FilterFn fn, int* returnSize) {
    int* out = (int*)malloc((size_t)arrSize * sizeof(int));
    int n = 0;
    for (int i = 0; i < arrSize; i++) if (fn(arr[i], i)) out[n++] = arr[i];
    *returnSize = n;
    return out;
}
