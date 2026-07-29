// LeetCode 1377 - Frog Position After T Seconds
// https://leetcode.com/problems/frog-position-after-t-seconds/

#include <stdlib.h>

double frogPosition(int n, int** edges, int edgesSize, int* edgesColSize, int t, int target) {
    (void)edgesColSize;
    int** g = (int**)malloc((n + 1) * sizeof(int*));
    int* gSize = (int*)calloc(n + 1, sizeof(int));
    int* gCap = (int*)calloc(n + 1, sizeof(int));
    for (int i = 0; i <= n; i++) { gCap[i] = 4; g[i] = (int*)malloc(4 * sizeof(int)); }
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        if (gSize[a] == gCap[a]) { gCap[a] *= 2; g[a] = (int*)realloc(g[a], gCap[a] * sizeof(int)); }
        if (gSize[b] == gCap[b]) { gCap[b] *= 2; g[b] = (int*)realloc(g[b], gCap[b] * sizeof(int)); }
        g[a][gSize[a]++] = b;
        g[b][gSize[b]++] = a;
    }
    typedef struct { int u, p, time; double prob; } Frame;
    Frame* st = (Frame*)malloc((n + 5) * sizeof(Frame));
    int top = 0;
    st[top++] = (Frame){1, 0, 0, 1.0};
    double result = 0;
    while (top) {
        Frame f = st[--top];
        int kn = 0;
        for (int i = 0; i < gSize[f.u]; i++) if (g[f.u][i] != f.p) kn++;
        if (f.time == t || kn == 0) {
            if (f.u == target) result += f.prob;
            continue;
        }
        for (int i = 0; i < gSize[f.u]; i++) {
            int v = g[f.u][i];
            if (v == f.p) continue;
            st[top++] = (Frame){v, f.u, f.time + 1, f.prob / kn};
        }
    }
    free(st);
    for (int i = 0; i <= n; i++) free(g[i]);
    free(g); free(gSize); free(gCap);
    return result;
}
