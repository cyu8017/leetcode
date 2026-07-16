// LeetCode 0051 - N-Queens
// https://leetcode.com/problems/n-queens/

#include <stdlib.h>
#include <string.h>

typedef struct {
    char** board;
    int n;
} BoardSnapshot;

static int g_n;
static int* g_cols;
static int* g_diag1;
static int* g_diag2;
static char** g_board;
static BoardSnapshot* g_result;
static int g_resultCount;
static int g_resultCapacity;

static char* makeRow(int n, int queenCol) {
    char* row = (char*)malloc((size_t)n + 1);
    for (int i = 0; i < n; i++) {
        row[i] = i == queenCol ? 'Q' : '.';
    }
    row[n] = '\0';
    return row;
}

static void addSnapshot(void) {
    if (g_resultCount >= g_resultCapacity) {
        g_resultCapacity = g_resultCapacity == 0 ? 8 : g_resultCapacity * 2;
        g_result = (BoardSnapshot*)realloc(g_result, (size_t)g_resultCapacity * sizeof(BoardSnapshot));
    }

    char** boardCopy = (char**)malloc((size_t)g_n * sizeof(char*));
    for (int i = 0; i < g_n; i++) {
        boardCopy[i] = (char*)malloc((size_t)g_n + 1);
        memcpy(boardCopy[i], g_board[i], (size_t)g_n + 1);
    }

    g_result[g_resultCount].board = boardCopy;
    g_result[g_resultCount].n = g_n;
    g_resultCount++;
}

static void backtrack(int row) {
    if (row == g_n) {
        addSnapshot();
        return;
    }

    for (int col = 0; col < g_n; col++) {
        if (g_cols[col] || g_diag1[row + col] || g_diag2[row - col + g_n - 1]) {
            continue;
        }

        g_cols[col] = 1;
        g_diag1[row + col] = 1;
        g_diag2[row - col + g_n - 1] = 1;

        free(g_board[row]);
        g_board[row] = makeRow(g_n, col);

        backtrack(row + 1);

        g_cols[col] = 0;
        g_diag1[row + col] = 0;
        g_diag2[row - col + g_n - 1] = 0;
        free(g_board[row]);
        g_board[row] = makeRow(g_n, -1);
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced by caller.
 */
char*** solveNQueens(int n, int* returnSize, int** returnColumnSizes) {
    g_n = n;
    g_result = NULL;
    g_resultCount = 0;
    g_resultCapacity = 0;

    g_cols = (int*)calloc((size_t)n, sizeof(int));
    g_diag1 = (int*)calloc((size_t)(2 * n), sizeof(int));
    g_diag2 = (int*)calloc((size_t)(2 * n), sizeof(int));
    g_board = (char**)malloc((size_t)n * sizeof(char*));
    for (int i = 0; i < n; i++) {
        g_board[i] = makeRow(n, -1);
    }

    backtrack(0);

    char*** result = (char***)malloc((size_t)g_resultCount * sizeof(char**));
    int* colSizes = (int*)malloc((size_t)g_resultCount * sizeof(int));
    for (int i = 0; i < g_resultCount; i++) {
        result[i] = g_result[i].board;
        colSizes[i] = n;
    }

    free(g_result);
    free(g_cols);
    free(g_diag1);
    free(g_diag2);
    for (int i = 0; i < n; i++) {
        free(g_board[i]);
    }
    free(g_board);

    *returnSize = g_resultCount;
    *returnColumnSizes = colSizes;
    return result;
}
