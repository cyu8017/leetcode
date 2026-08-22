// LeetCode 3424 - Minimum Cost to Make Arrays Identical
// https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

#include <stdlib.h>
#include <string.h>

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

long long minCost(int* arr, int arrSize, int* brr, int brrSize, long long k) {
    (void)brrSize;
    long long noSwap = 0;
    for (int i = 0; i < arrSize; i++) {
        long long d = arr[i] - brr[i]; if (d < 0) d = -d; noSwap += d;
    }
    int* a2 = (int*)malloc(arrSize * sizeof(int));
    int* b2 = (int*)malloc(arrSize * sizeof(int));
    memcpy(a2, arr, arrSize * sizeof(int));
    memcpy(b2, brr, arrSize * sizeof(int));
    qsort(a2, arrSize, sizeof(int), cmp_int);
    qsort(b2, arrSize, sizeof(int), cmp_int);
    long long withSwap = k;
    for (int i = 0; i < arrSize; i++) {
        long long d = a2[i] - b2[i]; if (d < 0) d = -d; withSwap += d;
    }
    free(a2); free(b2);
    return noSwap < withSwap ? noSwap : withSwap;
}
