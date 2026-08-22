// LeetCode 2943 - Maximize Area of Square Hole in Grid
// https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return (*(const int*)a) - (*(const int*)b); }

static int maxGap(int* bars, int barsSize) {
    if (barsSize == 0) return 1;
    qsort(bars, barsSize, sizeof(int), cmp_int);
    int best = 1, cur = 1;
    for (int i = 1; i < barsSize; i++) {
        if (bars[i] == bars[i - 1] + 1) cur++;
        else cur = 1;
        if (cur > best) best = cur;
    }
    return best + 1;
}

int maximizeSquareHoleArea(int n, int m, int* hBars, int hBarsSize, int* vBars, int vBarsSize) {
    (void)n; (void)m;
    int side = maxGap(hBars, hBarsSize);
    int vs = maxGap(vBars, vBarsSize);
    if (vs < side) side = vs;
    return side * side;
}
