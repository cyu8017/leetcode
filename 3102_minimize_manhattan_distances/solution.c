// LeetCode 3102 - Minimize Manhattan Distances
// https://leetcode.com/problems/minimize-manhattan-distances/

#include <stdlib.h>
#include <string.h>
#include <limits.h>

static int cmp_int(const void* a, const void* b) { return (*(const int*)a) - (*(const int*)b); }
static int imax(int a, int b) { return a > b ? a : b; }

int minimumDistance(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize;
    int n = pointsSize;
    int* s1 = (int*)malloc((size_t)n * sizeof(int));
    int* s2 = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) {
        s1[i] = points[i][0] + points[i][1];
        s2[i] = points[i][0] - points[i][1];
    }
    int* a1 = (int*)malloc((size_t)n * sizeof(int));
    int* a2 = (int*)malloc((size_t)n * sizeof(int));
    memcpy(a1, s1, (size_t)n * sizeof(int));
    memcpy(a2, s2, (size_t)n * sizeof(int));
    qsort(a1, (size_t)n, sizeof(int), cmp_int);
    qsort(a2, (size_t)n, sizeof(int), cmp_int);
    int ans = INT_MAX;
    for (int i = 0; i < n; i++) {
        int v1 = s1[i], v2 = s2[i];
        int mn1 = (a1[0] == v1 && (n < 2 || a1[1] != v1)) ? a1[1] : a1[0];
        int mx1 = (a1[n - 1] == v1 && (n < 2 || a1[n - 2] != v1)) ? a1[n - 2] : a1[n - 1];
        int mn2 = (a2[0] == v2 && (n < 2 || a2[1] != v2)) ? a2[1] : a2[0];
        int mx2 = (a2[n - 1] == v2 && (n < 2 || a2[n - 2] != v2)) ? a2[n - 2] : a2[n - 1];
        int cur = imax(mx1 - mn1, mx2 - mn2);
        if (cur < ans) ans = cur;
    }
    free(s1); free(s2); free(a1); free(a2);
    return ans;
}
