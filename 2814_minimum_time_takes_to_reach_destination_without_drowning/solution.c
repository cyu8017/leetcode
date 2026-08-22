// LeetCode 2814 - Minimum Time Takes to Reach Destination Without Drowning
// https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/

#include <stdlib.h>
#include <string.h>

int minimumSeconds(char*** land, int landSize, int* landColSize) {
    int m = landSize, n = landColSize[0];
    const int INF = 1 << 30;
    int** water = (int**)malloc(m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        water[i] = (int*)malloc(n * sizeof(int));
        for (int j = 0; j < n; j++) water[i][j] = INF;
    }
    int* qx = (int*)malloc(m * n * sizeof(int));
    int* qy = (int*)malloc(m * n * sizeof(int));
    int qh = 0, qt = 0;
    int sx = 0, sy = 0, dx = 0, dy = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            char* cell = land[i][j];
            if (cell[0] == '*') { water[i][j] = 0; qx[qt] = i; qy[qt] = j; qt++; }
            else if (cell[0] == 'S') { sx = i; sy = j; }
            else if (cell[0] == 'D') { dx = i; dy = j; }
        }
    }
    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
    while (qh < qt) {
        int x = qx[qh], y = qy[qh]; qh++;
        for (int d = 0; d < 4; d++) {
            int ni = x + dirs[d][0], nj = y + dirs[d][1];
            if (ni < 0 || nj < 0 || ni >= m || nj >= n) continue;
            char c = land[ni][nj][0];
            if (c == 'X' || c == 'D') continue;
            if (water[ni][nj] > water[x][y] + 1) {
                water[ni][nj] = water[x][y] + 1;
                qx[qt] = ni; qy[qt] = nj; qt++;
            }
        }
    }
    int** dist = (int**)malloc(m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        dist[i] = (int*)malloc(n * sizeof(int));
        for (int j = 0; j < n; j++) dist[i][j] = -1;
    }
    qh = qt = 0;
    qx[qt] = sx; qy[qt] = sy; qt++;
    dist[sx][sy] = 0;
    int ans = -1;
    while (qh < qt) {
        int x = qx[qh], y = qy[qh]; qh++;
        if (x == dx && y == dy) { ans = dist[x][y]; break; }
        for (int d = 0; d < 4; d++) {
            int ni = x + dirs[d][0], nj = y + dirs[d][1];
            if (ni < 0 || nj < 0 || ni >= m || nj >= n || dist[ni][nj] != -1) continue;
            if (land[ni][nj][0] == 'X') continue;
            int nd = dist[x][y] + 1;
            if (land[ni][nj][0] != 'D' && nd >= water[ni][nj]) continue;
            dist[ni][nj] = nd;
            qx[qt] = ni; qy[qt] = nj; qt++;
        }
    }
    for (int i = 0; i < m; i++) { free(water[i]); free(dist[i]); }
    free(water); free(dist); free(qx); free(qy);
    return ans;
}
