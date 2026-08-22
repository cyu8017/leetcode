// LeetCode 2906 - Construct Product Matrix
// https://leetcode.com/problems/construct-product-matrix/

#include <stdlib.h>

int** constructProductMatrix(int** grid, int gridSize, int* gridColSize, int* returnSize, int** returnColumnSizes) {
    const int mod = 12345;
    int m = gridSize, n = gridColSize[0];
    int** ans = (int**)malloc(m * sizeof(int*));
    *returnColumnSizes = (int*)malloc(m * sizeof(int));
    for (int i = 0; i < m; i++) {
        ans[i] = (int*)calloc(n, sizeof(int));
        (*returnColumnSizes)[i] = n;
    }
    long long pref = 1;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            ans[i][j] = (int)pref;
            pref = pref * (grid[i][j] % mod) % mod;
        }
    long long suf = 1;
    for (int i = m - 1; i >= 0; i--)
        for (int j = n - 1; j >= 0; j--) {
            ans[i][j] = (int)(ans[i][j] * suf % mod);
            suf = suf * (grid[i][j] % mod) % mod;
        }
    *returnSize = m;
    return ans;
}
