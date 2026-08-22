// LeetCode 0348 - Design Tic-Tac-Toe
// https://leetcode.com/problems/design-tic-tac-toe/

#include <stdlib.h>

typedef struct {
    int n;
    int* rows;
    int* cols;
    int diag;
    int antiDiag;
} TicTacToe;

TicTacToe* ticTacToeCreate(int n) {
    TicTacToe* obj = (TicTacToe*)calloc(1, sizeof(TicTacToe));
    obj->n = n;
    obj->rows = (int*)calloc((size_t)n, sizeof(int));
    obj->cols = (int*)calloc((size_t)n, sizeof(int));
    return obj;
}

int ticTacToeMove(TicTacToe* obj, int row, int col, int player) {
    int add = player == 1 ? 1 : -1;

    obj->rows[row] += add;
    obj->cols[col] += add;
    if (row == col) {
        obj->diag += add;
    }
    if (row + col == obj->n - 1) {
        obj->antiDiag += add;
    }

    if (obj->rows[row] == obj->n || obj->rows[row] == -obj->n
        || obj->cols[col] == obj->n || obj->cols[col] == -obj->n
        || obj->diag == obj->n || obj->diag == -obj->n
        || obj->antiDiag == obj->n || obj->antiDiag == -obj->n) {
        return player;
    }

    return 0;
}

void ticTacToeFree(TicTacToe* obj) {
    free(obj->rows);
    free(obj->cols);
    free(obj);
}
