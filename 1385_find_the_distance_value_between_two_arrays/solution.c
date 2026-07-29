// LeetCode 1385 - Find the Distance Value Between Two Arrays
// https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int findTheDistanceValue(int* arr1, int arr1Size, int* arr2, int arr2Size, int d) {
    int* b = (int*)malloc(arr2Size * sizeof(int));
    for (int i = 0; i < arr2Size; i++) b[i] = arr2[i];
    qsort(b, arr2Size, sizeof(int), cmp_int);
    int ans = 0;
    for (int i = 0; i < arr1Size; i++) {
        int x = arr1[i];
        int lo = 0, hi = arr2Size;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (b[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        int ok = 1;
        if (lo < arr2Size) {
            int diff = b[lo] - x; if (diff < 0) diff = -diff;
            if (diff <= d) ok = 0;
        }
        if (ok && lo > 0) {
            int diff = b[lo - 1] - x; if (diff < 0) diff = -diff;
            if (diff <= d) ok = 0;
        }
        ans += ok;
    }
    free(b);
    return ans;
}
