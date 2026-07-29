// LeetCode 0885 - Spiral Matrix III
// https://leetcode.com/problems/spiral-matrix-iii/

#include <stdlib.h>

int** spiralMatrixIII(int rows, int cols, int rStart, int cStart, int* returnSize, int** returnColumnSizes) {
    int total = rows * cols;
    int** ans = (int**)malloc((size_t)total * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)total * sizeof(int));
    for (int i = 0; i < total; i++) {
        ans[i] = (int*)malloc(2 * sizeof(int));
        (*returnColumnSizes)[i] = 2;
    }
    ans[0][0] = rStart; ans[0][1] = cStart;
    if (total == 1) { *returnSize = 1; return ans; }
    int r = rStart, c = cStart, count = 1;
    int dirs[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
    int steps = 1;
    while (count < total) {
        for (int d = 0; d < 4; d++) {
            for (int s = 0; s < steps; s++) {
                r += dirs[d][0];
                c += dirs[d][1];
                if (r >= 0 && r < rows && c >= 0 && c < cols) {
                    ans[count][0] = r;
                    ans[count][1] = c;
                    count++;
                    if (count == total) { *returnSize = total; return ans; }
                }
            }
            if (d % 2 == 1) steps++;
        }
    }
    *returnSize = total;
    return ans;
}
