// LeetCode 2577 - Minimum Time to Visit a Cell In a Grid
// https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

#include <stdlib.h>

typedef struct { int t, r, c; } Item;

static void siftUp(Item* h, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p].t <= h[i].t) break;
        Item tmp = h[p]; h[p] = h[i]; h[i] = tmp;
        i = p;
    }
}
static void siftDown(Item* h, int n, int i) {
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, best = i;
        if (l < n && h[l].t < h[best].t) best = l;
        if (r < n && h[r].t < h[best].t) best = r;
        if (best == i) break;
        Item tmp = h[i]; h[i] = h[best]; h[best] = tmp;
        i = best;
    }
}

int minimumTime(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    if (grid[0][1] > 1 && grid[1][0] > 1) return -1;
    int** dist = (int**)malloc((size_t)m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        dist[i] = (int*)malloc((size_t)n * sizeof(int));
        for (int j = 0; j < n; j++) dist[i][j] = 1 << 30;
    }
    int cap = m * n * 4 + 16;
    Item* heap = (Item*)malloc((size_t)cap * sizeof(Item));
    int hs = 0;
    heap[hs++] = (Item){0, 0, 0};
    dist[0][0] = 0;
    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
    while (hs > 0) {
        Item cur = heap[0];
        heap[0] = heap[--hs];
        if (hs) siftDown(heap, hs, 0);
        if (cur.r == m - 1 && cur.c == n - 1) {
            int ans = cur.t;
            for (int i = 0; i < m; i++) free(dist[i]);
            free(dist); free(heap);
            return ans;
        }
        if (cur.t > dist[cur.r][cur.c]) continue;
        for (int d = 0; d < 4; d++) {
            int nr = cur.r + dirs[d][0], nc = cur.c + dirs[d][1];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            int nt = cur.t + 1;
            if (nt < grid[nr][nc]) {
                int wait = grid[nr][nc] - nt;
                if (wait % 2 == 1) wait++;
                nt += wait;
            }
            if (nt < dist[nr][nc]) {
                dist[nr][nc] = nt;
                if (hs >= cap) {
                    cap *= 2;
                    heap = (Item*)realloc(heap, (size_t)cap * sizeof(Item));
                }
                heap[hs] = (Item){nt, nr, nc};
                siftUp(heap, hs);
                hs++;
            }
        }
    }
    for (int i = 0; i < m; i++) free(dist[i]);
    free(dist); free(heap);
    return -1;
}
