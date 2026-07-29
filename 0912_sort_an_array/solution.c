// LeetCode 0912 - Sort an Array
// https://leetcode.com/problems/sort-an-array/

#include <stdlib.h>
#include <string.h>

static void mergeSort(int* a, int* tmp, int l, int r) {
    if (r - l <= 1) return;
    int m = (l + r) / 2;
    mergeSort(a, tmp, l, m);
    mergeSort(a, tmp, m, r);
    int i = l, j = m, k = l;
    while (i < m && j < r) tmp[k++] = a[i] <= a[j] ? a[i++] : a[j++];
    while (i < m) tmp[k++] = a[i++];
    while (j < r) tmp[k++] = a[j++];
    for (i = l; i < r; i++) a[i] = tmp[i];
}

int* sortArray(int* nums, int numsSize, int* returnSize) {
    int* tmp = (int*)malloc((size_t)numsSize * sizeof(int));
    mergeSort(nums, tmp, 0, numsSize);
    free(tmp);
    *returnSize = numsSize;
    return nums;
}
