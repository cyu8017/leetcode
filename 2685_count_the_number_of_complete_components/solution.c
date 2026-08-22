// LeetCode 2685 - Count the Number of Complete Components
// https://leetcode.com/problems/count-the-number-of-complete-components/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int countCompleteComponents(int n, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* gSz = (int*)calloc((size_t)n, sizeof(int));
    int* gCap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        for (int t = 0; t < 2; t++) {
            int a = t ? v : u, b = t ? u : v;
            if (gSz[a] == gCap[a]) {
                gCap[a] = gCap[a] ? gCap[a] * 2 : 4;
                g[a] = (int*)realloc(g[a], (size_t)gCap[a] * sizeof(int));
            }
            g[a][gSz[a]++] = b;
        }
    }
    bool* seen = (bool*)calloc((size_t)n, sizeof(bool));
    int ans = 0;
    int* stack = (int*)malloc((size_t)n * sizeof(int));
    int* nodes = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) {
        if (seen[i]) continue;
        int top = 0, nsz = 0, edgeCnt = 0;
        stack[top++] = i;
        seen[i] = true;
        while (top > 0) {
            int u = stack[--top];
            nodes[nsz++] = u;
            edgeCnt += gSz[u];
            for (int j = 0; j < gSz[u]; j++) {
                int v = g[u][j];
                if (!seen[v]) { seen[v] = true; stack[top++] = v; }
            }
        }
        if (edgeCnt / 2 == nsz * (nsz - 1) / 2) ans++;
    }
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gSz); free(gCap); free(seen); free(stack); free(nodes);
    return ans;
}
