// LeetCode 3283 - Maximum Number of Moves to Kill All Pawns
// https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/

#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <stdbool.h>

static int* knightDist(int x, int y, int pts[][2], int np) {
    static const int dirs[8][2] = {{1,2},{1,-2},{-1,2},{-1,-2},{2,1},{2,-1},{-2,1},{-2,-1}};
    int* ans = (int*)malloc((size_t)np * sizeof(int));
    for (int i = 0; i < np; i++) ans[i] = -1;
    bool vis[50][50];
    memset(vis, 0, sizeof(vis));
    int qx[2500], qy[2500], qd[2500];
    int qh = 0, qt = 0;
    qx[qt] = x; qy[qt] = y; qd[qt] = 0; qt++;
    vis[x][y] = true;
    int found = 0;
    while (qh < qt && found < np) {
        int cx = qx[qh], cy = qy[qh], cd = qd[qh];
        qh++;
        for (int i = 0; i < np; i++) {
            if (ans[i] == -1 && pts[i][0] == cx && pts[i][1] == cy) {
                ans[i] = cd;
                found++;
            }
        }
        for (int d = 0; d < 8; d++) {
            int nx = cx + dirs[d][0], ny = cy + dirs[d][1];
            if (nx < 0 || ny < 0 || nx >= 50 || ny >= 50 || vis[nx][ny]) continue;
            vis[nx][ny] = true;
            qx[qt] = nx; qy[qt] = ny; qd[qt] = cd + 1; qt++;
        }
    }
    return ans;
}

static int g_n3283, g_N3283;
static int** g_dist3283;
static int** g_memo3283;

static int dfs3283(int mask, int cur, int turn) {
    if (mask == g_N3283 - 1) return 0;
    if (g_memo3283[mask][cur] != -1) return g_memo3283[mask][cur];
    int best = turn == 0 ? INT_MIN / 4 : INT_MAX / 4;
    for (int i = 0; i < g_n3283; i++) {
        if (mask & (1 << i)) continue;
        int d = g_dist3283[cur][i + 1];
        int v = d + dfs3283(mask | (1 << i), i + 1, 1 - turn);
        if (turn == 0) {
            if (v > best) best = v;
        } else if (v < best) {
            best = v;
        }
    }
    g_memo3283[mask][cur] = best;
    return best;
}

int maxMoves(int kx, int ky, int** positions, int positionsSize, int* positionsColSize) {
    (void)positionsColSize;
    int n = positionsSize;
    int pts[17][2];
    pts[0][0] = kx;
    pts[0][1] = ky;
    for (int i = 0; i < n; i++) {
        pts[i + 1][0] = positions[i][0];
        pts[i + 1][1] = positions[i][1];
    }
    int* dist[17];
    for (int i = 0; i <= n; i++) dist[i] = knightDist(pts[i][0], pts[i][1], pts, n + 1);
    int N = 1 << n;
    int** memo = (int**)malloc((size_t)N * sizeof(int*));
    for (int i = 0; i < N; i++) {
        memo[i] = (int*)malloc((size_t)(n + 1) * sizeof(int));
        for (int j = 0; j <= n; j++) memo[i][j] = -1;
    }
    g_n3283 = n;
    g_N3283 = N;
    g_dist3283 = dist;
    g_memo3283 = memo;
    int ans = dfs3283(0, 0, 0);
    for (int i = 0; i <= n; i++) free(dist[i]);
    for (int i = 0; i < N; i++) free(memo[i]);
    free(memo);
    return ans;
}
