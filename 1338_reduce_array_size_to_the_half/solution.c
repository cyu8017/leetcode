// LeetCode 1338 - Reduce Array Size to The Half
// https://leetcode.com/problems/reduce-array-size-to-the-half/

#include <stdlib.h>

static int cmp_desc(const void* a, const void* b) { return *(const int*)b - *(const int*)a; }
static int cmp_asc(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int minSetSize(int* arr, int arrSize) {
    int* sorted = (int*)malloc(arrSize * sizeof(int));
    for (int i = 0; i < arrSize; i++) sorted[i] = arr[i];
    qsort(sorted, arrSize, sizeof(int), cmp_asc);
    int* freqs = (int*)malloc(arrSize * sizeof(int));
    int fn = 0, i = 0;
    while (i < arrSize) {
        int j = i;
        while (j < arrSize && sorted[j] == sorted[i]) j++;
        freqs[fn++] = j - i;
        i = j;
    }
    qsort(freqs, fn, sizeof(int), cmp_desc);
    int removed = 0;
    for (int c = 0; c < fn; c++) {
        removed += freqs[c];
        if (removed * 2 >= arrSize) {
            free(sorted); free(freqs);
            return c + 1;
        }
    }
    free(sorted); free(freqs);
    return 0;
}
