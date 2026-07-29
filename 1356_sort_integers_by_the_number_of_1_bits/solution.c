// LeetCode 1356 - Sort Integers by The Number of 1 Bits
// https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

#include <stdlib.h>

static int bitcount(int x) {
    int c = 0;
    while (x) { c += x & 1; x >>= 1; }
    return c;
}
static int cmp_bits(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    int bx = bitcount(x), by = bitcount(y);
    if (bx != by) return bx - by;
    return x - y;
}

int* sortByBits(int* arr, int arrSize, int* returnSize) {
    int* ans = (int*)malloc(arrSize * sizeof(int));
    for (int i = 0; i < arrSize; i++) ans[i] = arr[i];
    qsort(ans, arrSize, sizeof(int), cmp_bits);
    *returnSize = arrSize;
    return ans;
}
