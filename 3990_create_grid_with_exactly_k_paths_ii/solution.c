// LeetCode 3990 - Create Grid With Exactly K Paths II
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-ii/

#include <stdlib.h>
#include <string.h>

static int bitWidth(unsigned k) {
    int w = 0;
    while (k) { ++w; k >>= 1; }
    return w;
}

char** createGrid(int k, int* returnSize) {
    if (k <= 0) { *returnSize = 0; return NULL; }
    int l = bitWidth((unsigned)k);
    int m = 2 * l, n = l + 3;
    char** result = (char**)malloc((size_t)m * sizeof(char*));
    for (int i = 0; i < m; i++) {
        result[i] = (char*)malloc((size_t)n + 1);
        memset(result[i], '#', (size_t)n);
        result[i][n] = '\0';
    }
    for (int i = 0; i < l; i++) {
        int r = 2 * i;
        result[r][i] = result[r][i + 1] = result[r + 1][i] = result[r + 1][i + 1] = '.';
        if (k & (1 << i)) {
            for (int c = i + 2; c < n; c++) result[r][c] = '.';
        }
    }
    for (int r = 0; r < m; r++) result[r][n - 1] = '.';
    *returnSize = m;
    return result;
}
