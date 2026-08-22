// LeetCode 2258 - Escape the Spreading Fire
// https://leetcode.com/problems/escape-the-spreading-fire/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static bool can_wait(int wait, int** grid, int m, int n, int** fire, int dirs[4][2]) {
    const int inf = 1000000000;
    if (wait >= fire[0][0]) return false;
    bool** vis = (bool**)malloc((size_t)m * sizeof(bool*));
    for (int i = 0; i < m; i++) vis[i] = (bool*)calloc((size_t)n, sizeof(bool));
    int* qr = (int*)malloc((size_t)m * n * sizeof(int));
    int* qc = (int*)malloc((size_t)m * n * sizeof(int));
    int* qt = (int*)malloc((size_t)m * n * sizeof(int));
    int head = 0, tail = 0;
    qr[tail] = 0; qc[tail] = 0; qt[tail] = wait; tail++;
    vis[0][0] = true;
    bool ok = false;
    while (head < tail) {
        int r = qr[head], c = qc[head], t = qt[head];
        head++;
        for (int d = 0; d < 4; d++) {
            int nr = r + dirs[d][0], nc = c + dirs[d][1], nt = t + 1;
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 2 || vis[nr][nc]) continue;
            if (nr == m - 1 && nc == n - 1) {
                if (nt <= fire[nr][nc]) { ok = true; break; }
                continue;
            }
            if (nt >= fire[nr][nc]) continue;
            vis[nr][nc] = true;
            qr[tail] = nr; qc[tail] = nc; qt[tail] = nt; tail++;
        }
        if (ok) break;
    }
    for (int i = 0; i < m; i++) free(vis[i]);
    free(vis); free(qr); free(qc); free(qt);
    return ok;
}

int maximumMinutes(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    const int inf = 1000000000;
    int** fire = (int**)malloc((size_t)m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        fire[i] = (int*)malloc((size_t)n * sizeof(int));
        for (int j = 0; j < n; j++) fire[i][j] = inf;
    }
    int* qr = (int*)malloc((size_t)m * n * sizeof(int));
    int* qc = (int*)malloc((size_t)m * n * sizeof(int));
    int head = 0, tail = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            if (grid[i][j] == 1) {
                fire[i][j] = 0;
                qr[tail] = i; qc[tail] = j; tail++;
            }
    int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    while (head < tail) {
        int r = qr[head], c = qc[head]; head++;
        for (int d = 0; d < 4; d++) {
            int nr = r + dirs[d][0], nc = c + dirs[d][1];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 2 || fire[nr][nc] != inf) continue;
            fire[nr][nc] = fire[r][c] + 1;
            qr[tail] = nr; qc[tail] = nc; tail++;
        }
    }
    free(qr); free(qc);
    int lo = 0, hi = m * n + 10, ans = -1;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if (can_wait(mid, grid, m, n, fire, dirs)) {
            ans = mid;
            lo = mid + 1;
        } else hi = mid - 1;
    }
    for (int i = 0; i < m; i++) free(fire[i]);
    free(fire);
    if (ans >= m * n) return inf;
    return ans;
}
