// LeetCode 1466 - Reorder Routes to Make All Paths Lead to the City Zero
// https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

#include <stdlib.h>
#include <stdbool.h>

int minReorder(int n, int** connections, int connectionsSize, int* connectionsColSize) {
    (void)connectionsColSize;
    int** to = (int**)malloc(n * sizeof(int*));
    int** cost = (int**)malloc(n * sizeof(int*));
    int* sz = (int*)calloc(n, sizeof(int));
    int* cap = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; i++) { cap[i] = 4; to[i] = (int*)malloc(4 * sizeof(int)); cost[i] = (int*)malloc(4 * sizeof(int)); }
    for (int i = 0; i < connectionsSize; i++) {
        int a = connections[i][0], b = connections[i][1];
        if (sz[a] == cap[a]) { cap[a] *= 2; to[a] = (int*)realloc(to[a], cap[a]*sizeof(int)); cost[a] = (int*)realloc(cost[a], cap[a]*sizeof(int)); }
        if (sz[b] == cap[b]) { cap[b] *= 2; to[b] = (int*)realloc(to[b], cap[b]*sizeof(int)); cost[b] = (int*)realloc(cost[b], cap[b]*sizeof(int)); }
        to[a][sz[a]] = b; cost[a][sz[a]++] = 1;
        to[b][sz[b]] = a; cost[b][sz[b]++] = 0;
    }
    bool* seen = (bool*)calloc(n, sizeof(bool));
    int* stack = (int*)malloc(n * sizeof(int));
    int top = 0; stack[top++] = 0; seen[0] = true;
    int ans = 0;
    while (top) {
        int node = stack[--top];
        for (int i = 0; i < sz[node]; i++) {
            int nei = to[node][i];
            if (!seen[nei]) { seen[nei] = true; stack[top++] = nei; ans += cost[node][i]; }
        }
    }
    for (int i = 0; i < n; i++) { free(to[i]); free(cost[i]); }
    free(to); free(cost); free(sz); free(cap); free(seen); free(stack);
    return ans;
}
