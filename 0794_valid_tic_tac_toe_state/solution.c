// LeetCode 0794 - Valid Tic-Tac-Toe State
#include <stdbool.h>
#include <string.h>

static bool win(char** board, char p) {
    for (int i = 0; i < 3; i++) {
        if (board[i][0]==p && board[i][1]==p && board[i][2]==p) return true;
        if (board[0][i]==p && board[1][i]==p && board[2][i]==p) return true;
    }
    if (board[0][0]==p && board[1][1]==p && board[2][2]==p) return true;
    if (board[0][2]==p && board[1][1]==p && board[2][0]==p) return true;
    return false;
}

bool validTicTacToe(char** board, int boardSize) {
    (void)boardSize;
    int x = 0, o = 0;
    for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) {
        if (board[i][j] == 'X') x++;
        if (board[i][j] == 'O') o++;
    }
    if (!(o == x || o == x - 1)) return false;
    bool xw = win(board, 'X'), ow = win(board, 'O');
    if (xw && ow) return false;
    if (xw && x != o + 1) return false;
    if (ow && x != o) return false;
    return true;
}
