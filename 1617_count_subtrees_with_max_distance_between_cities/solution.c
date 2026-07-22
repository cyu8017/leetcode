// LeetCode 1617 - Count Subtrees With Max Distance Between Cities
// https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

#include <stdlib.h>
#include <string.h>

int* countSubgraphsForEachDiameter(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    (void)edgesColSize;
    int** adj = (int**)malloc((size_t)n * sizeof(int*));
    int* deg = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) adj[i] = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0] - 1, b = edges[i][1] - 1;
        adj[a][deg[a]++] = b;
        adj[b][deg[b]++] = a;
    }
    int* ans = (int*)calloc((size_t)(n - 1), sizeof(int));
    *returnSize = n - 1;
    int dist[15], q[15];
    for (int mask = 1; mask < (1 << n); mask++) {
        if ((mask & (mask - 1)) == 0) continue;
        int start = 0;
        while (!(mask & (1 << start))) start++;
        int bits = 0;
        for (int t = mask; t; t &= t - 1) bits++;

        memset(dist, -1, sizeof(dist));
        int front = 0, back = 0;
        q[back++] = start; dist[start] = 0;
        while (front < back) {
            int u = q[front++];
            for (int i = 0; i < deg[u]; i++) {
                int v = adj[u][i];
                if ((mask & (1 << v)) && dist[v] < 0) {
                    dist[v] = dist[u] + 1;
                    q[back++] = v;
                }
            }
        }
        if (back != bits) continue;
        int far = start;
        for (int i = 0; i < n; i++) if (dist[i] > dist[far]) far = i;

        memset(dist, -1, sizeof(dist));
        front = back = 0;
        q[back++] = far; dist[far] = 0;
        while (front < back) {
            int u = q[front++];
            for (int i = 0; i < deg[u]; i++) {
                int v = adj[u][i];
                if ((mask & (1 << v)) && dist[v] < 0) {
                    dist[v] = dist[u] + 1;
                    q[back++] = v;
                }
            }
        }
        int diameter = 0;
        for (int i = 0; i < n; i++) if (dist[i] > diameter) diameter = dist[i];
        if (diameter > 0) ans[diameter - 1]++;
    }
    for (int i = 0; i < n; i++) free(adj[i]);
    free(adj); free(deg);
    return ans;
}
