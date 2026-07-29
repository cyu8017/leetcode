// LeetCode 1471 - The k Strongest Values in an Array
// https://leetcode.com/problems/the-k-strongest-values-in-an-array/

#include <stdlib.h>

static int median_g;
static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }
static int cmp_strong(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    int ax = x - median_g; if (ax < 0) ax = -ax;
    int ay = y - median_g; if (ay < 0) ay = -ay;
    if (ax != ay) return ay - ax;
    return y - x;
}

int* getStrongest(int* arr, int arrSize, int k, int* returnSize) {
    qsort(arr, arrSize, sizeof(int), cmp_int);
    median_g = arr[(arrSize - 1) / 2];
    qsort(arr, arrSize, sizeof(int), cmp_strong);
    int* ans = (int*)malloc(k * sizeof(int));
    for (int i = 0; i < k; i++) ans[i] = arr[i];
    *returnSize = k;
    return ans;
}
