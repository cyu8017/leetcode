// LeetCode 2596 - Check Knight Tour Configuration
// https://leetcode.com/problems/check-knight-tour-configuration/

#include <stdlib.h>
#include <stdbool.h>

bool checkValidGrid(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    int n = gridSize;
    if (grid[0][0] != 0) return false;
    int* posr = (int*)malloc((size_t)(n * n) * sizeof(int));
    int* posc = (int*)malloc((size_t)(n * n) * sizeof(int));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            posr[grid[i][j]] = i;
            posc[grid[i][j]] = j;
        }
    int dirs[8][2] = {{1,2},{1,-2},{-1,2},{-1,-2},{2,1},{2,-1},{-2,1},{-2,-1}};
    for (int v = 0; v + 1 < n * n; v++) {
        int r = posr[v], c = posc[v];
        bool ok = false;
        for (int d = 0; d < 8; d++) {
            if (r + dirs[d][0] == posr[v + 1] && c + dirs[d][1] == posc[v + 1]) { ok = true; break; }
        }
        if (!ok) { free(posr); free(posc); return false; }
    }
    free(posr); free(posc);
    return true;
}
