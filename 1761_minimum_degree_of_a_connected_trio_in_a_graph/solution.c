// LeetCode 1761 - Minimum Degree of a Connected Trio in a Graph
// https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

#include <limits.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int minTrioDegree(int n, int** edges, int edgesSize, int* edgesColSize) {
    bool* adj = (bool*)calloc((size_t)n * n, sizeof(bool));
    int* degree = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0] - 1;
        int v = edges[i][1] - 1;
        adj[u * n + v] = true;
        adj[v * n + u] = true;
        degree[u]++;
        degree[v]++;
    }
    int best = INT_MAX;
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0] - 1;
        int v = edges[i][1] - 1;
        for (int k = 0; k < n; k++) {
            if (adj[u * n + k] && adj[v * n + k]) {
                int total = degree[u] + degree[v] + degree[k] - 6;
                if (total < best) {
                    best = total;
                }
            }
        }
    }
    free(adj);
    free(degree);
    return best == INT_MAX ? -1 : best;
}
