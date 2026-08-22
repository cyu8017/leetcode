// LeetCode 3218 - Minimum Cost for Cutting Cake I
// https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/

#include <stdlib.h>

static int cmp_rev(const void* a, const void* b) { return *(const int*)b - *(const int*)a; }

int minimumCost(int m, int n, int* horizontalCut, int horizontalCutSize, int* verticalCut, int verticalCutSize) {
    (void)horizontalCutSize; (void)verticalCutSize;
    qsort(horizontalCut, m - 1, sizeof(int), cmp_rev);
    qsort(verticalCut, n - 1, sizeof(int), cmp_rev);
    int ans = 0, i = 0, j = 0, h = 1, v = 1;
    while (i < m - 1 || j < n - 1) {
        if (j == n - 1 || (i < m - 1 && horizontalCut[i] > verticalCut[j])) {
            ans += horizontalCut[i] * v; h++; i++;
        } else {
            ans += verticalCut[j] * h; v++; j++;
        }
    }
    return ans;
}
