// LeetCode 0827 - Making A Large Island
// https://leetcode.com/problems/making-a-large-island/

#include <stdlib.h>

#define MAX(a,b) ((a)>(b)?(a):(b))

static int dfs(int** grid, int n, int r, int c, int iid) {
    if (r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1) return 0;
    grid[r][c] = iid;
    return 1 + dfs(grid, n, r + 1, c, iid) + dfs(grid, n, r - 1, c, iid)
             + dfs(grid, n, r, c + 1, iid) + dfs(grid, n, r, c - 1, iid);
}

int largestIsland(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    int n = gridSize;
    int* sizes = (int*)calloc((size_t)(n * n + 3), sizeof(int));
    int island_id = 2;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (grid[i][j] == 1) {
                sizes[island_id] = dfs(grid, n, i, j, island_id);
                island_id++;
            }
    int ans = 0;
    for (int id = 2; id < island_id; id++) ans = MAX(ans, sizes[id]);
    int dr[4] = {1,-1,0,0}, dc[4] = {0,0,1,-1};
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] != 0) continue;
            int seen[4], ns = 0, total = 1;
            for (int k = 0; k < 4; k++) {
                int ni = i + dr[k], nj = j + dc[k];
                if (ni < 0 || ni >= n || nj < 0 || nj >= n) continue;
                int iid = grid[ni][nj];
                if (iid <= 1) continue;
                int dup = 0;
                for (int t = 0; t < ns; t++) if (seen[t] == iid) { dup = 1; break; }
                if (!dup) { seen[ns++] = iid; total += sizes[iid]; }
            }
            ans = MAX(ans, total);
        }
    }
    free(sizes);
    return ans == 0 ? n * n : ans;
}
