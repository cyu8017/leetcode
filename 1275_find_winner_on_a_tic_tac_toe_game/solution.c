// LeetCode 1275 - Find Winner on a Tic Tac Toe Game
// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

#include <stdlib.h>
#include <string.h>

char* tictactoe(int** moves, int movesSize, int* movesColSize) {
    (void)movesColSize;
    int board[3][3] = {{0}};
    for (int i = 0; i < movesSize; i++) {
        int r = moves[i][0], c = moves[i][1];
        board[r][c] = (i % 2 == 0) ? 1 : -1;
    }
    for (int i = 0; i < 3; i++) {
        int rs = board[i][0] + board[i][1] + board[i][2];
        int cs = board[0][i] + board[1][i] + board[2][i];
        if (rs == 3 || cs == 3) {
            char* ans = (char*)malloc(2);
            ans[0] = 'A';
            ans[1] = '\0';
            return ans;
        }
        if (rs == -3 || cs == -3) {
            char* ans = (char*)malloc(2);
            ans[0] = 'B';
            ans[1] = '\0';
            return ans;
        }
    }
    if (board[0][0] + board[1][1] + board[2][2] == 3 || board[0][2] + board[1][1] + board[2][0] == 3) {
        char* ans = (char*)malloc(2);
        ans[0] = 'A';
        ans[1] = '\0';
        return ans;
    }
    if (board[0][0] + board[1][1] + board[2][2] == -3 || board[0][2] + board[1][1] + board[2][0] == -3) {
        char* ans = (char*)malloc(2);
        ans[0] = 'B';
        ans[1] = '\0';
        return ans;
    }
    char* ans = (char*)malloc(8);
    strcpy(ans, movesSize == 9 ? "Draw" : "Pending");
    return ans;
}
