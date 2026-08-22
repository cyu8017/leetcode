// LeetCode 2127 - Maximum Employees to Be Invited to a Meeting
// https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

#include <stdlib.h>
#include <stdbool.h>

int maximumInvitations(int* favorite, int favoriteSize) {
    int n = favoriteSize;
    int* indeg = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) indeg[favorite[i]]++;
    int* depth = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) depth[i] = 1;
    int* q = (int*)malloc((size_t)n * sizeof(int));
    int qh = 0, qt = 0;
    for (int i = 0; i < n; i++) if (indeg[i] == 0) q[qt++] = i;
    while (qh < qt) {
        int u = q[qh++];
        int v = favorite[u];
        if (depth[u] + 1 > depth[v]) depth[v] = depth[u] + 1;
        if (--indeg[v] == 0) q[qt++] = v;
    }
    int pairSum = 0, maxCycle = 0;
    bool* vis = (bool*)calloc((size_t)n, sizeof(bool));
    for (int i = 0; i < n; i++) {
        if (indeg[i] == 0 || vis[i]) continue;
        int u = i, lenCycle = 0;
        while (!vis[u]) { vis[u] = true; u = favorite[u]; lenCycle++; }
        if (lenCycle == 2) pairSum += depth[i] + depth[favorite[i]];
        else if (lenCycle > maxCycle) maxCycle = lenCycle;
    }
    free(indeg); free(depth); free(q); free(vis);
    return pairSum > maxCycle ? pairSum : maxCycle;
}
