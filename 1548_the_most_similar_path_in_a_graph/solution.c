// LeetCode 1548 - The Most Similar Path in a Graph
// https://leetcode.com/problems/the-most-similar-path-in-a-graph/

#include <stdlib.h>
#include <string.h>

int* mostSimilar(int n, int** roads, int roadsSize, int* roadsColSize, char** names, int namesSize, char** targetPath, int targetPathSize, int* returnSize) {
    (void)roadsColSize; (void)namesSize;
    int* head = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) head[i] = -1;
    int* to = (int*)malloc((size_t)roadsSize * 2 * sizeof(int));
    int* next = (int*)malloc((size_t)roadsSize * 2 * sizeof(int));
    int ec = 0;
    for (int i = 0; i < roadsSize; i++) {
        int a = roads[i][0], b = roads[i][1];
        to[ec] = b; next[ec] = head[a]; head[a] = ec++;
        to[ec] = a; next[ec] = head[b]; head[b] = ec++;
    }

    int* cost = (int*)malloc((size_t)n * sizeof(int));
    int** path = (int**)malloc((size_t)n * sizeof(int*));
    for (int node = 0; node < n; node++) {
        cost[node] = strcmp(names[node], targetPath[0]) != 0;
        path[node] = (int*)malloc(sizeof(int));
        path[node][0] = node;
    }

    for (int i = 1; i < targetPathSize; i++) {
        int* ncost = (int*)malloc((size_t)n * sizeof(int));
        int** npath = (int**)malloc((size_t)n * sizeof(int*));
        for (int node = 0; node < n; node++) {
            int bestCost = 1000000000, bestPrev = -1;
            for (int e = head[node]; e != -1; e = next[e]) {
                int prev = to[e];
                if (cost[prev] < bestCost) {
                    bestCost = cost[prev];
                    bestPrev = prev;
                }
            }
            ncost[node] = bestCost + (strcmp(names[node], targetPath[i]) != 0);
            npath[node] = (int*)malloc((size_t)(i + 1) * sizeof(int));
            memcpy(npath[node], path[bestPrev], (size_t)i * sizeof(int));
            npath[node][i] = node;
        }
        for (int node = 0; node < n; node++) free(path[node]);
        free(path); free(cost);
        path = npath; cost = ncost;
    }

    int best = 0;
    for (int node = 1; node < n; node++) if (cost[node] < cost[best]) best = node;
    int* ans = (int*)malloc((size_t)targetPathSize * sizeof(int));
    memcpy(ans, path[best], (size_t)targetPathSize * sizeof(int));
    *returnSize = targetPathSize;

    for (int node = 0; node < n; node++) free(path[node]);
    free(path); free(cost); free(head); free(to); free(next);
    return ans;
}
