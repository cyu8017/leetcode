// LeetCode 3004 - Maximum Subtree of the Same Color
// https://leetcode.com/problems/maximum-subtree-of-the-same-color/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static int ans3004;
static int* size3004;
static int* colors3004;
static int** g3004;
static int* gsz3004;

static bool dfs3004(int a, int fa) {
    size3004[a] = 1;
    bool ok = true;
    for (int i = 0; i < gsz3004[a]; i++) {
        int b = g3004[a][i];
        if (b == fa) continue;
        bool t = dfs3004(b, a);
        ok = ok && t && colors3004[a] == colors3004[b];
        size3004[a] += size3004[b];
    }
    if (ok && size3004[a] > ans3004) ans3004 = size3004[a];
    return ok;
}

int maximumSubtreeSize(int** edges, int edgesSize, int* edgesColSize, int* colors, int colorsSize) {
    (void)edgesColSize; (void)colorsSize;
    int n = edgesSize + 1;
    g3004 = (int**)calloc((size_t)n, sizeof(int*));
    gsz3004 = (int*)calloc((size_t)n, sizeof(int));
    int* cap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        if (gsz3004[a] == cap[a]) {
            cap[a] = cap[a] ? cap[a] * 2 : 2;
            g3004[a] = (int*)realloc(g3004[a], (size_t)cap[a] * sizeof(int));
        }
        if (gsz3004[b] == cap[b]) {
            cap[b] = cap[b] ? cap[b] * 2 : 2;
            g3004[b] = (int*)realloc(g3004[b], (size_t)cap[b] * sizeof(int));
        }
        g3004[a][gsz3004[a]++] = b;
        g3004[b][gsz3004[b]++] = a;
    }
    size3004 = (int*)calloc((size_t)n, sizeof(int));
    colors3004 = colors;
    ans3004 = 0;
    dfs3004(0, -1);
    for (int i = 0; i < n; i++) free(g3004[i]);
    free(g3004); free(gsz3004); free(cap); free(size3004);
    return ans3004;
}
