// LeetCode 3002 - Maximum Size of a Set After Removals
// https://leetcode.com/problems/maximum-size-of-a-set-after-removals/

#include <stdlib.h>
#include <stdbool.h>

static int cmp_int(const void* a, const void* b) { return (*(const int*)a) - (*(const int*)b); }
static int imin(int a, int b) { return a < b ? a : b; }

int maximumSetSize(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    (void)nums2Size;
    int* a1 = (int*)malloc((size_t)nums1Size * sizeof(int));
    int* a2 = (int*)malloc((size_t)nums1Size * sizeof(int));
    for (int i = 0; i < nums1Size; i++) { a1[i] = nums1[i]; a2[i] = nums2[i]; }
    qsort(a1, (size_t)nums1Size, sizeof(int), cmp_int);
    qsort(a2, (size_t)nums1Size, sizeof(int), cmp_int);
    int u1 = 0, u2 = 0;
    for (int i = 0; i < nums1Size; i++) if (i == 0 || a1[i] != a1[i-1]) a1[u1++] = a1[i];
    for (int i = 0; i < nums1Size; i++) if (i == 0 || a2[i] != a2[i-1]) a2[u2++] = a2[i];
    int only1 = 0, only2 = 0, both = 0;
    int i = 0, j = 0;
    while (i < u1 && j < u2) {
        if (a1[i] < a2[j]) { only1++; i++; }
        else if (a1[i] > a2[j]) { only2++; j++; }
        else { both++; i++; j++; }
    }
    only1 += u1 - i; only2 += u2 - j;
    int n = nums1Size;
    only1 = imin(only1, n / 2);
    only2 = imin(only2, n / 2);
    free(a1); free(a2);
    return imin(only1 + only2 + both, n);
}
