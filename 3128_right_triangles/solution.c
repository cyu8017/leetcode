// LeetCode 3128 - Right Triangles
// https://leetcode.com/problems/right-triangles/

#include <stdlib.h>

long long numberOfRightTriangles(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    int* rows = calloc(m, sizeof(int));
    int* cols = calloc(n, sizeof(int));
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) { rows[i] += grid[i][j]; cols[j] += grid[i][j]; }
    long long ans = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            if (grid[i][j] == 1) ans += (long long)(rows[i] - 1) * (cols[j] - 1);
    free(rows); free(cols);
    return ans;
}
