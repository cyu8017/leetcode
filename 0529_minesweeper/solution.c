// LeetCode 0529 - Minesweeper
// https://leetcode.com/problems/minesweeper/

#include <stdio.h>

static int countMines(char** board, int boardSize, int* boardColSize, int row, int col) {
    static const int directions[8][2] = {
        {-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1},
    };
    int total = 0;
    const int cols = boardColSize[0];
    for (int index = 0; index < 8; index++) {
        const int nextRow = row + directions[index][0];
        const int nextCol = col + directions[index][1];
        if (nextRow >= 0 && nextRow < boardSize && nextCol >= 0 && nextCol < cols &&
            board[nextRow][nextCol] == 'M') {
            total++;
        }
    }
    return total;
}

static void reveal(char** board, int boardSize, int* boardColSize, int row, int col) {
    const int cols = boardColSize[0];
    if (row < 0 || row >= boardSize || col < 0 || col >= cols || board[row][col] != 'E') {
        return;
    }
    const int mines = countMines(board, boardSize, boardColSize, row, col);
    if (mines == 0) {
        board[row][col] = 'B';
        static const int directions[8][2] = {
            {-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1},
        };
        for (int index = 0; index < 8; index++) {
            reveal(board, boardSize, boardColSize, row + directions[index][0],
                   col + directions[index][1]);
        }
    } else {
        board[row][col] = (char)('0' + mines);
    }
}

char** updateBoard(char** board, int boardSize, int* boardColSize, int* click, int clickSize,
                   int* returnSize, int** returnColumnSizes) {
    (void)clickSize;
    const int row = click[0];
    const int col = click[1];
    if (board[row][col] == 'M') {
        board[row][col] = 'X';
    } else {
        reveal(board, boardSize, boardColSize, row, col);
    }
    *returnSize = boardSize;
    *returnColumnSizes = boardColSize;
    return board;
}
