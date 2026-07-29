// LeetCode 1391 - Check if There is a Valid Path in a Grid
// https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

#include <stdbool.h>
#include <stdlib.h>

bool hasValidPath(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    int dirs[7][2][2] = {
        {{0,0},{0,0}},
        {{0,-1},{0,1}}, {{-1,0},{1,0}}, {{0,-1},{1,0}},
        {{0,1},{1,0}}, {{0,-1},{-1,0}}, {{0,1},{-1,0}}
    };
    bool* seen = (bool*)calloc(m * n, sizeof(bool));
    int* st = (int*)malloc(m * n * 2 * sizeof(int));
    int top = 0;
    st[top++] = 0; st[top++] = 0;
    seen[0] = true;
    while (top) {
        int c = st[--top], r = st[--top];
        if (r == m - 1 && c == n - 1) { free(seen); free(st); return true; }
        int type = grid[r][c];
        for (int t = 0; t < 2; t++) {
            int dr = dirs[type][t][0], dc = dirs[type][t][1];
            int x = r + dr, y = c + dc;
            if (x < 0 || x >= m || y < 0 || y >= n || seen[x * n + y]) continue;
            int nt = grid[x][y];
            int ok = 0;
            for (int u = 0; u < 2; u++)
                if (dirs[nt][u][0] == -dr && dirs[nt][u][1] == -dc) ok = 1;
            if (ok) {
                seen[x * n + y] = true;
                st[top++] = x; st[top++] = y;
            }
        }
    }
    free(seen); free(st);
    return false;
}
