// LeetCode 3219 - Minimum Cost for Cutting Cake II
// https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/

#include <stdlib.h>

static int cmp_rev3219(const void* a, const void* b) { return *(const int*)b - *(const int*)a; }

long long minimumCost(int m, int n, int* horizontalCut, int horizontalCutSize, int* verticalCut, int verticalCutSize) {
    (void)horizontalCutSize; (void)verticalCutSize;
    qsort(horizontalCut, m - 1, sizeof(int), cmp_rev3219);
    qsort(verticalCut, n - 1, sizeof(int), cmp_rev3219);
    long long ans = 0;
    int i = 0, j = 0, h = 1, v = 1;
    while (i < m - 1 || j < n - 1) {
        if (j == n - 1 || (i < m - 1 && horizontalCut[i] > verticalCut[j])) {
            ans += (long long)horizontalCut[i] * v; h++; i++;
        } else {
            ans += (long long)verticalCut[j] * h; v++; j++;
        }
    }
    return ans;
}
