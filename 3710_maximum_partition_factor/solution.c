// LeetCode 3710 - Maximum Partition Factor
// https://leetcode.com/problems/maximum-partition-factor/

#include <stdlib.h>
#include <stdbool.h>

static int dist(int** points, int i, int j) {
    int dx = points[i][0] - points[j][0];
    int dy = points[i][1] - points[j][1];
    if (dx < 0) dx = -dx;
    if (dy < 0) dy = -dy;
    return dx + dy;
}

static bool ok(int** points, int n, int d) {
    int** g = (int**)malloc((size_t)n * sizeof(int*));
    int* gn = (int*)calloc((size_t)n, sizeof(int));
    int* gcap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) g[i] = NULL;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (dist(points, i, j) < d) {
                if (gn[i] == gcap[i]) {
                    gcap[i] = gcap[i] ? gcap[i] * 2 : 4;
                    g[i] = (int*)realloc(g[i], (size_t)gcap[i] * sizeof(int));
                }
                if (gn[j] == gcap[j]) {
                    gcap[j] = gcap[j] ? gcap[j] * 2 : 4;
                    g[j] = (int*)realloc(g[j], (size_t)gcap[j] * sizeof(int));
                }
                g[i][gn[i]++] = j;
                g[j][gn[j]++] = i;
            }
        }
    }
    int* color = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) color[i] = -1;
    int* q = (int*)malloc((size_t)n * sizeof(int));
    bool good = true;
    for (int i = 0; i < n && good; i++) {
        if (color[i] != -1) continue;
        int qh = 0, qt = 0;
        q[qt++] = i;
        color[i] = 0;
        while (qh < qt) {
            int u = q[qh++];
            for (int t = 0; t < gn[u]; t++) {
                int v = g[u][t];
                if (color[v] == -1) {
                    color[v] = color[u] ^ 1;
                    q[qt++] = v;
                } else if (color[v] == color[u]) {
                    good = false;
                    break;
                }
            }
            if (!good) break;
        }
    }
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gn); free(gcap); free(color); free(q);
    return good;
}

int maxPartitionFactor(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize;
    int n = pointsSize;
    if (n == 2) return 0;
    int lo = 0, hi = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int d = dist(points, i, j);
            if (d > hi) hi = d;
        }
    }
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        if (ok(points, n, mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
