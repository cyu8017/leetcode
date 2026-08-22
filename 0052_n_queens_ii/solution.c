// LeetCode 0052 - N-Queens II
// https://leetcode.com/problems/n-queens-ii/

#include <stdlib.h>

static int g_n;
static int* g_cols;
static int* g_diag1;
static int* g_diag2;
static int g_count;

static void backtrack(int row) {
    if (row == g_n) {
        g_count++;
        return;
    }

    for (int col = 0; col < g_n; col++) {
        if (g_cols[col] || g_diag1[row + col] || g_diag2[row - col + g_n - 1]) {
            continue;
        }

        g_cols[col] = 1;
        g_diag1[row + col] = 1;
        g_diag2[row - col + g_n - 1] = 1;
        backtrack(row + 1);
        g_cols[col] = 0;
        g_diag1[row + col] = 0;
        g_diag2[row - col + g_n - 1] = 0;
    }
}

int totalNQueens(int n) {
    g_n = n;
    g_count = 0;
    g_cols = (int*)calloc((size_t)n, sizeof(int));
    g_diag1 = (int*)calloc((size_t)(2 * n), sizeof(int));
    g_diag2 = (int*)calloc((size_t)(2 * n), sizeof(int));

    backtrack(0);

    free(g_cols);
    free(g_diag1);
    free(g_diag2);
    return g_count;
}
