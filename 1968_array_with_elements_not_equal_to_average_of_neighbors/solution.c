// LeetCode 1968 - Array With Elements Not Equal to Average of Neighbors
// https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int* rearrangeArray(int* nums, int numsSize, int* returnSize) {
    int* a = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) a[i] = nums[i];
    qsort(a, (size_t)numsSize, sizeof(int), cmpInt);
    int* res = (int*)malloc((size_t)numsSize * sizeof(int));
    int mid = (numsSize + 1) / 2;
    int i = 0, j = mid, k = 0;
    while (i < mid || j < numsSize) {
        if (i < mid) res[k++] = a[i++];
        if (j < numsSize) res[k++] = a[j++];
    }
    free(a);
    *returnSize = numsSize;
    return res;
}
