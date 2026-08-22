// LeetCode 2360 - Longest Cycle in a Graph
// https://leetcode.com/problems/longest-cycle-in-a-graph/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int longestCycle(int* edges, int edgesSize) {
    int n = edgesSize;
    bool* vis = (bool*)calloc((size_t)n, sizeof(bool));
    int* dist = (int*)malloc((size_t)n * sizeof(int));
    int ans = -1;
    for (int i = 0; i < n; i++) {
        if (vis[i]) continue;
        memset(dist, 0xFF, (size_t)n * sizeof(int)); /* -1 */
        int cur = i, step = 0;
        while (cur != -1 && !vis[cur]) {
            vis[cur] = true;
            dist[cur] = step;
            cur = edges[cur];
            step++;
        }
        if (cur != -1 && dist[cur] != -1) {
            int cycle = step - dist[cur];
            if (cycle > ans) ans = cycle;
        }
    }
    free(vis); free(dist);
    return ans;
}
