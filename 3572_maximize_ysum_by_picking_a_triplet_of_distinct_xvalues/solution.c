// LeetCode 3572 - Maximize Y-Sum by Picking a Triplet of Distinct X-Values
// https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int x, y; } Pair;
static int cmp_pair(const void* a, const void* b) {
    return ((const Pair*)b)->y - ((const Pair*)a)->y;
}

int maxSumDistinctTriplet(int* x, int xSize, int* y, int ySize) {
    (void)ySize;
    int n = xSize;
    Pair* arr = (Pair*)malloc((size_t)n * sizeof(Pair));
    for (int i = 0; i < n; i++) { arr[i].x = x[i]; arr[i].y = y[i]; }
    qsort(arr, (size_t)n, sizeof(Pair), cmp_pair);
    int ans = 0, seen[3], sc = 0;
    for (int i = 0; i < n; i++) {
        bool ok = true;
        for (int j = 0; j < sc; j++) if (seen[j] == arr[i].x) { ok = false; break; }
        if (ok) {
            seen[sc++] = arr[i].x;
            ans += arr[i].y;
            if (sc == 3) { free(arr); return ans; }
        }
    }
    free(arr);
    return -1;
}
