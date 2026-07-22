// LeetCode 1615 - Maximal Network Rank
// https://leetcode.com/problems/maximal-network-rank/

#include <stdlib.h>
#include <string.h>

int maximalNetworkRank(int n, int** roads, int roadsSize, int* roadsColSize) {
    (void)roadsColSize;
    int* degree = (int*)calloc((size_t)n, sizeof(int));
    char* edge = (char*)calloc((size_t)n * n, 1);
    for (int i = 0; i < roadsSize; i++) {
        int a = roads[i][0], b = roads[i][1];
        degree[a]++; degree[b]++;
        edge[a * n + b] = edge[b * n + a] = 1;
    }
    int ans = 0;
    for (int a = 0; a < n; a++) {
        for (int b = a + 1; b < n; b++) {
            int rank = degree[a] + degree[b] - edge[a * n + b];
            if (rank > ans) ans = rank;
        }
    }
    free(degree); free(edge);
    return ans;
}
