// LeetCode 2812 - Find the Safest Path in a Grid
// https://leetcode.com/problems/find-the-safest-path-in-a-grid/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int maximumSafenessFactor(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    int n = gridSize;
    int** dist = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        dist[i] = (int*)malloc(n * sizeof(int));
        for (int j = 0; j < n; j++) dist[i][j] = -1;
    }
    int* qx = (int*)malloc(n * n * sizeof(int));
    int* qy = (int*)malloc(n * n * sizeof(int));
    int qh = 0, qt = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (grid[i][j] == 1) {
                dist[i][j] = 0;
                qx[qt] = i; qy[qt] = j; qt++;
            }
    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
    while (qh < qt) {
        int x = qx[qh], y = qy[qh]; qh++;
        for (int d = 0; d < 4; d++) {
            int ni = x + dirs[d][0], nj = y + dirs[d][1];
            if (ni >= 0 && nj >= 0 && ni < n && nj < n && dist[ni][nj] == -1) {
                dist[ni][nj] = dist[x][y] + 1;
                qx[qt] = ni; qy[qt] = nj; qt++;
            }
        }
    }
    int* sx = (int*)malloc(n * n * sizeof(int));
    int* sy = (int*)malloc(n * n * sizeof(int));
    bool* seenflat = (bool*)malloc(n * n * sizeof(bool));
    int lo = 0, hi = n * n, ans = 0;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        int ok = 0;
        if (dist[0][0] >= mid) {
            memset(seenflat, 0, n * n);
            int top = 0;
            sx[top] = 0; sy[top] = 0; top++;
            seenflat[0] = true;
            while (top > 0) {
                top--;
                int x = sx[top], y = sy[top];
                if (x == n - 1 && y == n - 1) { ok = 1; break; }
                for (int d = 0; d < 4; d++) {
                    int ni = x + dirs[d][0], nj = y + dirs[d][1];
                    if (ni >= 0 && nj >= 0 && ni < n && nj < n && !seenflat[ni * n + nj] && dist[ni][nj] >= mid) {
                        seenflat[ni * n + nj] = true;
                        sx[top] = ni; sy[top] = nj; top++;
                    }
                }
            }
        }
        if (ok) { ans = mid; lo = mid + 1; }
        else hi = mid - 1;
    }
    for (int i = 0; i < n; i++) free(dist[i]);
    free(dist); free(qx); free(qy); free(sx); free(sy); free(seenflat);
    return ans;
}
