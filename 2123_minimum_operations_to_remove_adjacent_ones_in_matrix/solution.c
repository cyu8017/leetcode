// LeetCode 2123 - Minimum Operations to Remove Adjacent Ones in Matrix
// https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static bool dfsMatch(int u, int** g, int* gLen, int* matchR, bool* seen, int cnt) {
    for (int i = 0; i < gLen[u]; i++) {
        int v = g[u][i];
        if (seen[v]) continue;
        seen[v] = true;
        if (matchR[v] == -1 || dfsMatch(matchR[v], g, gLen, matchR, seen, cnt)) {
            matchR[v] = u;
            return true;
        }
    }
    return false;
}

int minimumOperations(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    int** id = (int**)malloc((size_t)m * sizeof(int*));
    int cnt = 0;
    for (int i = 0; i < m; i++) {
        id[i] = (int*)malloc((size_t)n * sizeof(int));
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) id[i][j] = cnt++;
            else id[i][j] = -1;
        }
    }
    int** g = (int**)calloc((size_t)cnt, sizeof(int*));
    int* gLen = (int*)calloc((size_t)cnt, sizeof(int));
    int* gCap = (int*)calloc((size_t)cnt, sizeof(int));
    int dirs[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] != 1 || (i + j) % 2 != 0) continue;
            int u = id[i][j];
            for (int d = 0; d < 4; d++) {
                int ni = i + dirs[d][0], nj = j + dirs[d][1];
                if (ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] == 1) {
                    if (gLen[u] == gCap[u]) {
                        gCap[u] = gCap[u] ? gCap[u] * 2 : 4;
                        g[u] = (int*)realloc(g[u], (size_t)gCap[u] * sizeof(int));
                    }
                    g[u][gLen[u]++] = id[ni][nj];
                }
            }
        }
    }
    int* matchR = (int*)malloc((size_t)cnt * sizeof(int));
    for (int i = 0; i < cnt; i++) matchR[i] = -1;
    int ans = 0;
    for (int u = 0; u < cnt; u++) {
        bool ok = false;
        for (int i = 0; i < m && !ok; i++)
            for (int j = 0; j < n; j++)
                if (id[i][j] == u && (i + j) % 2 == 0) { ok = true; break; }
        if (!ok) continue;
        bool* seen = (bool*)calloc((size_t)cnt, sizeof(bool));
        if (dfsMatch(u, g, gLen, matchR, seen, cnt)) ans++;
        free(seen);
    }
    for (int i = 0; i < m; i++) free(id[i]);
    free(id);
    for (int i = 0; i < cnt; i++) free(g[i]);
    free(g); free(gLen); free(gCap); free(matchR);
    return ans;
}
