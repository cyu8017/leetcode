// LeetCode 1460 - Make Two Arrays Equal by Reversing Subarrays
// https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

#include <stdbool.h>
#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

bool canBeEqual(int* target, int targetSize, int* arr, int arrSize) {
    if (targetSize != arrSize) return false;
    int* a = (int*)malloc(targetSize * sizeof(int));
    int* b = (int*)malloc(arrSize * sizeof(int));
    for (int i = 0; i < targetSize; i++) { a[i] = target[i]; b[i] = arr[i]; }
    qsort(a, targetSize, sizeof(int), cmp_int);
    qsort(b, arrSize, sizeof(int), cmp_int);
    bool ok = true;
    for (int i = 0; i < targetSize; i++) if (a[i] != b[i]) { ok = false; break; }
    free(a); free(b);
    return ok;
}
