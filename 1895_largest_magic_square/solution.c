// LeetCode 1895 - Largest Magic Square
// https://leetcode.com/problems/largest-magic-square/

#include <stdbool.h>
#include <stdlib.h>

int largestMagicSquare(int** grid, int gridSize, int* gridColSize) {
    int rows = gridSize;
    int cols = gridColSize[0];
    int* rowPrefix = (int*)calloc((size_t)rows * (cols + 1), sizeof(int));
    int* colPrefix = (int*)calloc((size_t)cols * (rows + 1), sizeof(int));
    #define RP(r, c) rowPrefix[(r) * (cols + 1) + (c)]
    #define CP(c, r) colPrefix[(c) * (rows + 1) + (r)]

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            RP(i, j + 1) = RP(i, j) + grid[i][j];
            CP(j, i + 1) = CP(j, i) + grid[i][j];
        }
    }

    for (int size = rows < cols ? rows : cols; size >= 1; size--) {
        for (int rs = 0; rs + size <= rows; rs++) {
            for (int cs = 0; cs + size <= cols; cs++) {
                int target = RP(rs, cs + size) - RP(rs, cs);
                bool ok = true;
                for (int row = rs; row < rs + size; row++) {
                    if (RP(row, cs + size) - RP(row, cs) != target) {
                        ok = false;
                        break;
                    }
                }
                if (!ok) continue;
                for (int col = cs; col < cs + size; col++) {
                    if (CP(col, rs + size) - CP(col, rs) != target) {
                        ok = false;
                        break;
                    }
                }
                if (!ok) continue;
                int diag1 = 0, diag2 = 0;
                for (int offset = 0; offset < size; offset++) {
                    diag1 += grid[rs + offset][cs + offset];
                    diag2 += grid[rs + offset][cs + size - 1 - offset];
                }
                if (diag1 == target && diag2 == target) {
                    free(rowPrefix);
                    free(colPrefix);
                    return size;
                }
            }
        }
    }
    free(rowPrefix);
    free(colPrefix);
    return 1;
    #undef RP
    #undef CP
}
