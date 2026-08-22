// LeetCode 3669 - Balanced K-Factor Decomposition
// https://leetcode.com/problems/balanced-k-factor-decomposition/

#include <stdlib.h>
#include <limits.h>

#define MX 100001

static int* g_divs[MX];
static int g_divn[MX];
static int g_inited = 0;

static void ensureInit(void) {
    if (g_inited) return;
    g_inited = 1;
    for (int i = 1; i < MX; i++) g_divn[i] = 0;
    for (int i = 1; i < MX; i++) {
        for (int j = i; j < MX; j += i) g_divn[j]++;
    }
    for (int i = 1; i < MX; i++) {
        g_divs[i] = (int*)malloc((size_t)g_divn[i] * sizeof(int));
        g_divn[i] = 0;
    }
    for (int i = 1; i < MX; i++) {
        for (int j = i; j < MX; j += i) g_divs[j][g_divn[j]++] = i;
    }
}

static int curDiff;
static int* ansBuf;
static int* pathBuf;
static int kGlob;

static int imin(int a, int b) { return a < b ? a : b; }
static int imax(int a, int b) { return a > b ? a : b; }

static void dfs(int i, int x, int mi, int mx) {
    if (i == 0) {
        int d = imax(mx, x) - imin(mi, x);
        if (d < curDiff) {
            curDiff = d;
            pathBuf[i] = x;
            for (int t = 0; t < kGlob; t++) ansBuf[t] = pathBuf[t];
        }
        return;
    }
    for (int t = 0; t < g_divn[x]; t++) {
        int y = g_divs[x][t];
        pathBuf[i] = y;
        dfs(i - 1, x / y, imin(mi, y), imax(mx, y));
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minDifference(int n, int k, int* returnSize) {
    ensureInit();
    curDiff = INT_MAX;
    ansBuf = (int*)malloc((size_t)k * sizeof(int));
    pathBuf = (int*)malloc((size_t)k * sizeof(int));
    kGlob = k;
    dfs(k - 1, n, INT_MAX, 0);
    free(pathBuf);
    *returnSize = k;
    return ansBuf;
}
