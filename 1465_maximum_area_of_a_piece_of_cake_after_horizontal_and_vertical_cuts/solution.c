// LeetCode 1465 - Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
// https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int maxArea(int h, int w, int* horizontalCuts, int horizontalCutsSize, int* verticalCuts, int verticalCutsSize) {
    int* hs = (int*)malloc((horizontalCutsSize + 2) * sizeof(int));
    int* vs = (int*)malloc((verticalCutsSize + 2) * sizeof(int));
    hs[0] = 0; for (int i = 0; i < horizontalCutsSize; i++) hs[i + 1] = horizontalCuts[i]; hs[horizontalCutsSize + 1] = h;
    vs[0] = 0; for (int i = 0; i < verticalCutsSize; i++) vs[i + 1] = verticalCuts[i]; vs[verticalCutsSize + 1] = w;
    qsort(hs, horizontalCutsSize + 2, sizeof(int), cmp_int);
    qsort(vs, verticalCutsSize + 2, sizeof(int), cmp_int);
    int maxH = 0, maxV = 0;
    for (int i = 1; i < horizontalCutsSize + 2; i++) if (hs[i] - hs[i - 1] > maxH) maxH = hs[i] - hs[i - 1];
    for (int i = 1; i < verticalCutsSize + 2; i++) if (vs[i] - vs[i - 1] > maxV) maxV = vs[i] - vs[i - 1];
    free(hs); free(vs);
    return (int)(((long long)maxH * maxV) % 1000000007LL);
}
