// LeetCode 2662 - Minimum Cost of a Path With Special Roads
// https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

#include <stdlib.h>
#include <string.h>

typedef struct { int id, cost; } NC2662;

static int distMan2662(int* a, int* b) {
    int dx = a[0] - b[0], dy = a[1] - b[1];
    if (dx < 0) dx = -dx;
    if (dy < 0) dy = -dy;
    return dx + dy;
}

static void heapPush2662(NC2662* h, int* hs, NC2662 x) {
    int i = (*hs)++;
    h[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p].cost <= h[i].cost) break;
        NC2662 t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}

static NC2662 heapPop2662(NC2662* h, int* hs) {
    NC2662 top = h[0];
    h[0] = h[--(*hs)];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, sm = i;
        if (l < *hs && h[l].cost < h[sm].cost) sm = l;
        if (r < *hs && h[r].cost < h[sm].cost) sm = r;
        if (sm == i) break;
        NC2662 t = h[i]; h[i] = h[sm]; h[sm] = t;
        i = sm;
    }
    return top;
}

int minimumCost(int* start, int startSize, int* target, int targetSize, int** specialRoads, int specialRoadsSize, int* specialRoadsColSize) {
    (void)startSize; (void)targetSize; (void)specialRoadsColSize;
    int N = 2 + 2 * specialRoadsSize;
    int** points = (int**)malloc((size_t)N * sizeof(int*));
    for (int i = 0; i < N; i++) points[i] = (int*)malloc(2 * sizeof(int));
    points[0][0] = start[0]; points[0][1] = start[1];
    points[1][0] = target[0]; points[1][1] = target[1];
    for (int i = 0; i < specialRoadsSize; i++) {
        points[2 + 2 * i][0] = specialRoads[i][0];
        points[2 + 2 * i][1] = specialRoads[i][1];
        points[3 + 2 * i][0] = specialRoads[i][2];
        points[3 + 2 * i][1] = specialRoads[i][3];
    }
    int* gSz = (int*)calloc((size_t)N, sizeof(int));
    int* gCap = (int*)calloc((size_t)N, sizeof(int));
    NC2662** g = (NC2662**)calloc((size_t)N, sizeof(NC2662*));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) if (i != j) {
            if (gSz[i] == gCap[i]) {
                gCap[i] = gCap[i] ? gCap[i] * 2 : 8;
                g[i] = (NC2662*)realloc(g[i], (size_t)gCap[i] * sizeof(NC2662));
            }
            g[i][gSz[i]++] = (NC2662){j, distMan2662(points[i], points[j])};
        }
    }
    for (int ri = 0; ri < specialRoadsSize; ri++) {
        int* r = specialRoads[ri];
        int u = -1, v = -1;
        for (int i = 0; i < N; i++) {
            if (points[i][0] == r[0] && points[i][1] == r[1]) u = i;
            if (points[i][0] == r[2] && points[i][1] == r[3]) v = i;
        }
        if (u >= 0 && v >= 0) {
            if (gSz[u] == gCap[u]) {
                gCap[u] = gCap[u] ? gCap[u] * 2 : 8;
                g[u] = (NC2662*)realloc(g[u], (size_t)gCap[u] * sizeof(NC2662));
            }
            g[u][gSz[u]++] = (NC2662){v, r[4]};
        }
    }
    int* dist = (int*)malloc((size_t)N * sizeof(int));
    for (int i = 0; i < N; i++) dist[i] = 1 << 30;
    dist[0] = 0;
    NC2662* heap = (NC2662*)malloc((size_t)(N * N + 8) * sizeof(NC2662));
    int hs = 0;
    heapPush2662(heap, &hs, (NC2662){0, 0});
    while (hs > 0) {
        NC2662 cur = heapPop2662(heap, &hs);
        if (cur.cost > dist[cur.id]) continue;
        for (int i = 0; i < gSz[cur.id]; i++) {
            int nd = cur.cost + g[cur.id][i].cost;
            if (nd < dist[g[cur.id][i].id]) {
                dist[g[cur.id][i].id] = nd;
                heapPush2662(heap, &hs, (NC2662){g[cur.id][i].id, nd});
            }
        }
    }
    int ans = dist[1];
    for (int i = 0; i < N; i++) { free(points[i]); free(g[i]); }
    free(points); free(g); free(gSz); free(gCap); free(dist); free(heap);
    return ans;
}
