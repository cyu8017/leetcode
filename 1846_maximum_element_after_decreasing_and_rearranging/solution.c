// LeetCode 1846 - Maximum Element After Decreasing and Rearranging
// https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

int maximumElementAfterDecrementingAndRearranging(int* arr, int arrSize) {
    qsort(arr, (size_t)arrSize, sizeof(int), cmpInt);
    arr[0] = 1;
    for (int i = 1; i < arrSize; i++) {
        if (arr[i] > arr[i - 1] + 1) arr[i] = arr[i - 1] + 1;
    }
    int best = arr[0];
    for (int i = 1; i < arrSize; i++) {
        if (arr[i] > best) best = arr[i];
    }
    return best;
}
