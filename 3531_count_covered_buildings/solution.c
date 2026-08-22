// LeetCode 3531 - Count Covered Buildings
// https://leetcode.com/problems/count-covered-buildings/

#include <stdlib.h>

static int cmp_asc(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

int countCoveredBuildings(int n, int** buildings, int buildingsSize, int* buildingsColSize) {
    (void)n; (void)buildingsColSize;
    /* group by x and y using arrays of lists - n<=1e5 buildings, coords 1..n */
    int N = n + 1;
    int* c1 = (int*)calloc((size_t)N, sizeof(int));
    int* c2 = (int*)calloc((size_t)N, sizeof(int));
    for (int i = 0; i < buildingsSize; i++) {
        c1[buildings[i][0]]++;
        c2[buildings[i][1]]++;
    }
    int** g1 = (int**)calloc((size_t)N, sizeof(int*));
    int** g2 = (int**)calloc((size_t)N, sizeof(int*));
    int* p1 = (int*)calloc((size_t)N, sizeof(int));
    int* p2 = (int*)calloc((size_t)N, sizeof(int));
    for (int i = 1; i < N; i++) {
        if (c1[i]) g1[i] = (int*)malloc((size_t)c1[i] * sizeof(int));
        if (c2[i]) g2[i] = (int*)malloc((size_t)c2[i] * sizeof(int));
    }
    for (int i = 0; i < buildingsSize; i++) {
        int x = buildings[i][0], y = buildings[i][1];
        g1[x][p1[x]++] = y;
        g2[y][p2[y]++] = x;
    }
    for (int i = 1; i < N; i++) {
        if (c1[i]) qsort(g1[i], (size_t)c1[i], sizeof(int), cmp_asc);
        if (c2[i]) qsort(g2[i], (size_t)c2[i], sizeof(int), cmp_asc);
    }
    int ans = 0;
    for (int i = 0; i < buildingsSize; i++) {
        int x = buildings[i][0], y = buildings[i][1];
        int* l1 = g1[x]; int n1 = c1[x];
        int* l2 = g2[y]; int n2 = c2[y];
        if (l2[0] < x && x < l2[n2 - 1] && l1[0] < y && y < l1[n1 - 1]) ans++;
    }
    for (int i = 1; i < N; i++) { free(g1[i]); free(g2[i]); }
    free(g1); free(g2); free(c1); free(c2); free(p1); free(p2);
    return ans;
}
