// LeetCode 3548 - Equal Sum Grid Partition II
// https://leetcode.com/problems/equal-sum-grid-partition-ii/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

/* Use frequency map via sorting unique values - values up to 1e6 typically use hash */
typedef struct { long long k; int v; } KV;

static int findKV(KV* a, int n, long long k) {
    for (int i = 0; i < n; i++) if (a[i].k == k) return i;
    return -1;
}
static void addKV(KV* a, int* n, long long k, int d) {
    int i = findKV(a, *n, k);
    if (i < 0) { a[*n].k = k; a[*n].v = d; (*n)++; }
    else a[i].v += d;
}
static int getKV(KV* a, int n, long long k) {
    int i = findKV(a, n, k);
    return i < 0 ? 0 : a[i].v;
}

static bool check3548(int** g, int m, int n) {
    long long s1 = 0, s2 = 0;
    KV* cnt1 = (KV*)malloc((size_t)(m * n + 5) * sizeof(KV));
    KV* cnt2 = (KV*)malloc((size_t)(m * n + 5) * sizeof(KV));
    int n1 = 0, n2 = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            long long v = g[i][j];
            s2 += v;
            addKV(cnt2, &n2, v, 1);
        }
    for (int i = 0; i < m - 1; i++) {
        for (int j = 0; j < n; j++) {
            long long v = g[i][j];
            s1 += v; s2 -= v;
            addKV(cnt1, &n1, v, 1);
            addKV(cnt2, &n2, v, -1);
        }
        if (s1 == s2) { free(cnt1); free(cnt2); return true; }
        if (s1 < s2) {
            long long diff = s2 - s1;
            if (getKV(cnt2, n2, diff) > 0) {
                if ((m - i - 1 > 1 && n > 1) ||
                    (i == m - 2 && (g[i + 1][0] == diff || g[i + 1][n - 1] == diff)) ||
                    (n == 1 && (g[i + 1][0] == diff || g[m - 1][0] == diff))) {
                    free(cnt1); free(cnt2); return true;
                }
            }
        } else {
            long long diff = s1 - s2;
            if (getKV(cnt1, n1, diff) > 0) {
                if ((i + 1 > 1 && n > 1) ||
                    (i == 0 && (g[0][0] == diff || g[0][n - 1] == diff)) ||
                    (n == 1 && (g[0][0] == diff || g[i][0] == diff))) {
                    free(cnt1); free(cnt2); return true;
                }
            }
        }
    }
    free(cnt1); free(cnt2);
    return false;
}

static int** rotate3548(int** grid, int m, int n) {
    int** t = (int**)malloc((size_t)n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        t[i] = (int*)malloc((size_t)m * sizeof(int));
        for (int j = 0; j < m; j++) t[i][j] = grid[j][i];
    }
    return t;
}

bool canPartitionGrid(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    if (check3548(grid, m, n)) return true;
    int** rot = rotate3548(grid, m, n);
    bool ok = check3548(rot, n, m);
    for (int i = 0; i < n; i++) free(rot[i]);
    free(rot);
    return ok;
}
