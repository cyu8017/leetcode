// LeetCode 2959 - Number of Possible Sets of Closing Branches
// https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/

#include <stdlib.h>

int numberOfSets(int n, int maxDistance, int** roads, int roadsSize, int* roadsColSize) {
    (void)roadsColSize;
    int ans = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        int dist[15][15];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                dist[i][j] = (i == j) ? 0 : (1 << 29);
        for (int r = 0; r < roadsSize; r++) {
            int u = roads[r][0], v = roads[r][1], w = roads[r][2];
            if ((mask & (1 << u)) && (mask & (1 << v))) {
                if (w < dist[u][v]) { dist[u][v] = w; dist[v][u] = w; }
            }
        }
        for (int k = 0; k < n; k++) {
            if (!(mask & (1 << k))) continue;
            for (int i = 0; i < n; i++) {
                if (!(mask & (1 << i))) continue;
                for (int j = 0; j < n; j++) {
                    if (!(mask & (1 << j))) continue;
                    if (dist[i][k] + dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
        int ok = 1;
        for (int i = 0; i < n && ok; i++) {
            if (!(mask & (1 << i))) continue;
            for (int j = 0; j < n; j++) {
                if (!(mask & (1 << j))) continue;
                if (dist[i][j] > maxDistance) { ok = 0; break; }
            }
        }
        if (ok) ans++;
    }
    return ans;
}
