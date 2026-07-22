// LeetCode 1619 - Mean of Array After Removing Some Elements
// https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

double trimMean(int* arr, int arrSize) {
    qsort(arr, (size_t)arrSize, sizeof(int), cmpInt);
    int k = arrSize / 20;
    long long sum = 0;
    for (int i = k; i < arrSize - k; i++) sum += arr[i];
    return (double)sum / (arrSize - 2 * k);
}
