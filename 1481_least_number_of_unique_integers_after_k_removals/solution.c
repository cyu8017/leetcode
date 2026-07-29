// LeetCode 1481 - Least Number of Unique Integers after K Removals
// https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int findLeastNumOfUniqueInts(int* arr, int arrSize, int k) {
    int* sorted = (int*)malloc(arrSize * sizeof(int));
    for (int i = 0; i < arrSize; i++) sorted[i] = arr[i];
    qsort(sorted, arrSize, sizeof(int), cmp_int);
    int* counts = (int*)malloc(arrSize * sizeof(int));
    int cn = 0, i = 0;
    while (i < arrSize) {
        int j = i;
        while (j < arrSize && sorted[j] == sorted[i]) j++;
        counts[cn++] = j - i;
        i = j;
    }
    qsort(counts, cn, sizeof(int), cmp_int);
    int removed = 0;
    for (int t = 0; t < cn; t++) {
        if (k < counts[t]) break;
        k -= counts[t];
        removed++;
    }
    free(sorted); free(counts);
    return cn - removed;
}
