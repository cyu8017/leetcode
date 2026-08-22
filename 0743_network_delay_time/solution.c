// LeetCode 0743 - Network Delay Time
// https://leetcode.com/problems/network-delay-time/

#include <stdbool.h>
#include <stdlib.h>
#include <limits.h>

int networkDelayTime(int** times, int timesSize, int* timesColSize, int n, int k) {
    (void)timesColSize;
    int* dist = (int*)malloc((size_t)(n + 1) * sizeof(int));
    for (int i = 1; i <= n; i++) {
        dist[i] = INT_MAX;
    }
    dist[k] = 0;
    for (int iter = 0; iter < n - 1; iter++) {
        bool updated = false;
        for (int i = 0; i < timesSize; i++) {
            int u = times[i][0], v = times[i][1], w = times[i][2];
            if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                updated = true;
            }
        }
        if (!updated) {
            break;
        }
    }
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        if (dist[i] == INT_MAX) {
            free(dist);
            return -1;
        }
        if (dist[i] > ans) {
            ans = dist[i];
        }
    }
    free(dist);
    return ans;
}
