// LeetCode 1314 - Matrix Block Sum
// https://leetcode.com/problems/matrix-block-sum/

#include <stdlib.h>

int** matrixBlockSum(int** mat, int matSize, int* matColSize, int k, int* returnSize, int** returnColumnSizes) {
    int m = matSize, n = matColSize[0];
    int** prefix = (int**)malloc((m + 1) * sizeof(int*));
    for (int i = 0; i <= m; i++) prefix[i] = (int*)calloc(n + 1, sizeof(int));
    for (int r = 0; r < m; r++)
        for (int c = 0; c < n; c++)
            prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c];
    int** ans = (int**)malloc(m * sizeof(int*));
    *returnColumnSizes = (int*)malloc(m * sizeof(int));
    for (int r = 0; r < m; r++) {
        ans[r] = (int*)malloc(n * sizeof(int));
        (*returnColumnSizes)[r] = n;
        for (int c = 0; c < n; c++) {
            int r1 = r - k > 0 ? r - k : 0;
            int c1 = c - k > 0 ? c - k : 0;
            int r2 = r + k + 1 < m ? r + k + 1 : m;
            int c2 = c + k + 1 < n ? c + k + 1 : n;
            ans[r][c] = prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1];
        }
    }
    for (int i = 0; i <= m; i++) free(prefix[i]);
    free(prefix);
    *returnSize = m;
    return ans;
}
