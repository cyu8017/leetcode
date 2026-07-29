// LeetCode 0787 - Cheapest Flights Within K Stops
#include <stdlib.h>
#include <limits.h>

int findCheapestPrice(int n, int** flights, int flightsSize, int* flightsColSize, int src, int dst, int k) {
    (void)flightsColSize;
    int* dist = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) dist[i] = INT_MAX;
    dist[src] = 0;
    for (int iter = 0; iter <= k; iter++) {
        int* nxt = (int*)malloc((size_t)n * sizeof(int));
        for (int i = 0; i < n; i++) nxt[i] = dist[i];
        for (int i = 0; i < flightsSize; i++) {
            int u = flights[i][0], v = flights[i][1], price = flights[i][2];
            if (dist[u] != INT_MAX && dist[u] + price < nxt[v]) nxt[v] = dist[u] + price;
        }
        free(dist); dist = nxt;
    }
    int ans = dist[dst] == INT_MAX ? -1 : dist[dst];
    free(dist); return ans;
}
