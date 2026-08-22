// LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
// https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced, assume caller calls free().
 */
int** differenceOfDistinctValues(int** grid, int gridSize, int* gridColSize, int* returnSize, int** returnColumnSizes) {
    int m = gridSize, n = gridColSize[0];
    int** ans = (int**)malloc((size_t)m * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) {
        ans[i] = (int*)calloc((size_t)n, sizeof(int));
        (*returnColumnSizes)[i] = n;
    }
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            bool tl[51] = {0}, br[51] = {0};
            int ctl = 0, cbr = 0;
            for (int x = i - 1, y = j - 1; x >= 0 && y >= 0; x--, y--) {
                int v = grid[x][y];
                if (!tl[v]) { tl[v] = true; ctl++; }
            }
            for (int x = i + 1, y = j + 1; x < m && y < n; x++, y++) {
                int v = grid[x][y];
                if (!br[v]) { br[v] = true; cbr++; }
            }
            int d = ctl - cbr;
            if (d < 0) d = -d;
            ans[i][j] = d;
        }
    }
    *returnSize = m;
    return ans;
}
