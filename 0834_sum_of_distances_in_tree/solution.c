// LeetCode 0834 - Sum of Distances in Tree
// https://leetcode.com/problems/sum-of-distances-in-tree/

#include <stdlib.h>

static int** g;
static int* gsz;
static int* gcap;
static int* count;
static int* ans;
static int N;

static void add_edge(int a, int b) {
    if (gsz[a] == gcap[a]) {
        gcap[a] = gcap[a] ? gcap[a] * 2 : 2;
        g[a] = (int*)realloc(g[a], (size_t)gcap[a] * sizeof(int));
    }
    g[a][gsz[a]++] = b;
}

static void post(int node, int parent) {
    for (int i = 0; i < gsz[node]; i++) {
        int child = g[node][i];
        if (child == parent) continue;
        post(child, node);
        count[node] += count[child];
        ans[node] += ans[child] + count[child];
    }
}

static void reroot(int node, int parent) {
    for (int i = 0; i < gsz[node]; i++) {
        int child = g[node][i];
        if (child == parent) continue;
        ans[child] = ans[node] - count[child] + (N - count[child]);
        reroot(child, node);
    }
}

int* sumOfDistancesInTree(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    (void)edgesColSize;
    N = n;
    g = (int**)calloc((size_t)n, sizeof(int*));
    gsz = (int*)calloc((size_t)n, sizeof(int));
    gcap = (int*)calloc((size_t)n, sizeof(int));
    count = (int*)malloc((size_t)n * sizeof(int));
    ans = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) count[i] = 1;
    for (int i = 0; i < edgesSize; i++) {
        add_edge(edges[i][0], edges[i][1]);
        add_edge(edges[i][1], edges[i][0]);
    }
    post(0, -1);
    reroot(0, -1);
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gsz); free(gcap); free(count);
    *returnSize = n;
    return ans;
}
