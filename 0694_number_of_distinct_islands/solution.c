// LeetCode 0694 - Number of Distinct Islands
// https://leetcode.com/problems/number-of-distinct-islands/

#include <stdlib.h>
#include <string.h>

static void dfs(int** grid, int m, int n, int r, int c, int br, int bc, int* path, int* plen) {
    if (r < 0 || c < 0 || r >= m || c >= n || grid[r][c] == 0) return;
    grid[r][c] = 0;
    path[(*plen)++] = r - br;
    path[(*plen)++] = c - bc;
    dfs(grid, m, n, r + 1, c, br, bc, path, plen);
    dfs(grid, m, n, r - 1, c, br, bc, path, plen);
    dfs(grid, m, n, r, c + 1, br, bc, path, plen);
    dfs(grid, m, n, r, c - 1, br, bc, path, plen);
}

static int same(int* a, int alen, int* b, int blen) {
    if (alen != blen) return 0;
    for (int i = 0; i < alen; i++) if (a[i] != b[i]) return 0;
    return 1;
}

int numDistinctIslands(int** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0) return 0;
    int m = gridSize, n = gridColSize[0];
    int** shapes = (int**)malloc(1000 * sizeof(int*));
    int* shapeLens = (int*)malloc(1000 * sizeof(int));
    int shapeCount = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) {
                int* path = (int*)malloc((size_t)m * n * 2 * sizeof(int));
                int plen = 0;
                dfs(grid, m, n, i, j, i, j, path, &plen);
                int found = 0;
                for (int s = 0; s < shapeCount; s++) if (same(shapes[s], shapeLens[s], path, plen)) { found = 1; break; }
                if (!found) { shapes[shapeCount] = path; shapeLens[shapeCount] = plen; shapeCount++; }
                else free(path);
            }
        }
    }
    for (int s = 0; s < shapeCount; s++) free(shapes[s]);
    free(shapes); free(shapeLens);
    return shapeCount;
}
