// LeetCode 0851 - Loud and Rich
// https://leetcode.com/problems/loud-and-rich/

#include <stdlib.h>

static int** g;
static int* gsz;
static int* gcap;
static int* quiet;
static int* ans;

static void add_edge(int a, int b) {
    if (gsz[a] == gcap[a]) {
        gcap[a] = gcap[a] ? gcap[a] * 2 : 2;
        g[a] = (int*)realloc(g[a], (size_t)gcap[a] * sizeof(int));
    }
    g[a][gsz[a]++] = b;
}

static int dfs(int person) {
    if (ans[person] != -1) return ans[person];
    int best = person;
    for (int i = 0; i < gsz[person]; i++) {
        int cand = dfs(g[person][i]);
        if (quiet[cand] < quiet[best]) best = cand;
    }
    ans[person] = best;
    return best;
}

int* loudAndRich(int** richer, int richerSize, int* richerColSize, int* quietArr, int quietSize, int* returnSize) {
    (void)richerColSize;
    int n = quietSize;
    quiet = quietArr;
    g = (int**)calloc((size_t)n, sizeof(int*));
    gsz = (int*)calloc((size_t)n, sizeof(int));
    gcap = (int*)calloc((size_t)n, sizeof(int));
    ans = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) ans[i] = -1;
    for (int i = 0; i < richerSize; i++) add_edge(richer[i][1], richer[i][0]);
    for (int i = 0; i < n; i++) dfs(i);
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gsz); free(gcap);
    *returnSize = n;
    return ans;
}
