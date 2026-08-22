// LeetCode 2973 - Find Number of Coins to Place in Tree Nodes
// https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

#include <stdlib.h>
#include <string.h>

static int cmp2973(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

typedef struct {
    int* data;
    int size;
    int cap;
} Vec2973;

static void vecPush2973(Vec2973* v, int x) {
    if (v->size == v->cap) {
        v->cap = v->cap ? v->cap * 2 : 4;
        v->data = (int*)realloc(v->data, (size_t)v->cap * sizeof(int));
    }
    v->data[v->size++] = x;
}

static void dfs2973(int u, int p, Vec2973* g, int* cost, long long* ans, int** outVals, int* outSize) {
    Vec2973 vals = {0};
    vecPush2973(&vals, cost[u]);
    for (int i = 0; i < g[u].size; i++) {
        int v = g[u].data[i];
        if (v == p) continue;
        int* childVals = NULL;
        int childSize = 0;
        dfs2973(v, u, g, cost, ans, &childVals, &childSize);
        for (int j = 0; j < childSize; j++) vecPush2973(&vals, childVals[j]);
        free(childVals);
    }
    qsort(vals.data, (size_t)vals.size, sizeof(int), cmp2973);
    if (vals.size < 3) {
        ans[u] = 1;
    } else {
        int m = vals.size;
        long long cand1 = (long long)vals.data[m - 1] * vals.data[m - 2] * vals.data[m - 3];
        long long cand2 = (long long)vals.data[0] * vals.data[1] * vals.data[m - 1];
        long long best = cand1 > cand2 ? cand1 : cand2;
        if (best < 0) best = 0;
        ans[u] = best;
    }
    if (vals.size <= 5) {
        *outVals = vals.data;
        *outSize = vals.size;
        return;
    }
    int* keep = (int*)malloc(5 * sizeof(int));
    keep[0] = vals.data[0];
    keep[1] = vals.data[1];
    keep[2] = vals.data[vals.size - 3];
    keep[3] = vals.data[vals.size - 2];
    keep[4] = vals.data[vals.size - 1];
    free(vals.data);
    *outVals = keep;
    *outSize = 5;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* placedCoins(int** edges, int edgesSize, int* edgesColSize, int* cost, int costSize, int* returnSize) {
    (void)edgesColSize;
    int n = costSize;
    Vec2973* g = (Vec2973*)calloc((size_t)n, sizeof(Vec2973));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        vecPush2973(&g[u], v);
        vecPush2973(&g[v], u);
    }
    long long* ans = (long long*)malloc((size_t)n * sizeof(long long));
    int* rootVals = NULL;
    int rootSize = 0;
    dfs2973(0, -1, g, cost, ans, &rootVals, &rootSize);
    free(rootVals);
    for (int i = 0; i < n; i++) free(g[i].data);
    free(g);
    *returnSize = n;
    return ans;
}
