// LeetCode 3812 - Minimum Edge Toggles On A Tree
// https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct { int to, idx; } E3812;

static bool dfs3812(int a, int fa, int n, E3812** g, int* deg, char* start, char* target, int* ans, int* asz) {
    (void)n;
    bool rev = start[a] != target[a];
    for (int j = 0; j < deg[a]; j++) {
        int b = g[a][j].to, i = g[a][j].idx;
        if (b != fa && dfs3812(b, a, n, g, deg, start, target, ans, asz)) {
            ans[(*asz)++] = i;
            rev = !rev;
        }
    }
    return rev;
}

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int* minimumFlips(int n, int** edges, int edgesSize, int* edgesColSize, char* start, char* target, int* returnSize) {
    (void)edgesColSize; (void)edgesSize;
    E3812** g = (E3812**)calloc((size_t)n, sizeof(E3812*));
    int* deg = (int*)calloc((size_t)n, sizeof(int));
    int* cap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n - 1; i++) {
        int a = edges[i][0], b = edges[i][1];
        if (deg[a] == cap[a]) { cap[a] = cap[a] ? cap[a]*2 : 4; g[a] = (E3812*)realloc(g[a], (size_t)cap[a]*sizeof(E3812)); }
        g[a][deg[a]++] = (E3812){b, i};
        if (deg[b] == cap[b]) { cap[b] = cap[b] ? cap[b]*2 : 4; g[b] = (E3812*)realloc(g[b], (size_t)cap[b]*sizeof(E3812)); }
        g[b][deg[b]++] = (E3812){a, i};
    }
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int asz = 0;
    if (dfs3812(0, -1, n, g, deg, start, target, ans, &asz)) {
        ans[0] = -1;
        *returnSize = 1;
        for (int i = 0; i < n; i++) free(g[i]);
        free(g); free(deg); free(cap);
        return ans;
    }
    qsort(ans, (size_t)asz, sizeof(int), cmp_int);
    *returnSize = asz;
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(deg); free(cap);
    return ans;
}
