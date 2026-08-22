// LeetCode 1584 - Min Cost to Connect All Points
// https://leetcode.com/problems/min-cost-to-connect-all-points/

#include <stdlib.h>

int minCostConnectPoints(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize;
    int n = pointsSize;
    char* used = (char*)calloc((size_t)n, 1);
    int* dist = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) dist[i] = 1000000000;
    dist[0] = 0;
    int answer = 0;
    for (int iter = 0; iter < n; iter++) {
        int u = -1;
        for (int i = 0; i < n; i++) {
            if (!used[i] && (u < 0 || dist[i] < dist[u])) u = i;
        }
        used[u] = 1;
        answer += dist[u];
        for (int v = 0; v < n; v++) {
            if (!used[v]) {
                int d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1]);
                if (d < dist[v]) dist[v] = d;
            }
        }
    }
    free(used); free(dist);
    return answer;
}
