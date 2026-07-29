// LeetCode 1958 - Check if Move is Legal
// https://leetcode.com/problems/check-if-move-is-legal/

#include <stdbool.h>

bool checkMove(char** board, int boardSize, int* boardColSize, int rMove, int cMove, char color) {
    (void)boardColSize;
    int dirs[8][2] = {{1,0},{-1,0},{0,1},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}};
    char opp = color == 'W' ? 'B' : 'W';
    for (int d = 0; d < 8; d++) {
        int r = rMove + dirs[d][0], c = cMove + dirs[d][1];
        int len = 0;
        while (r >= 0 && c >= 0 && r < boardSize && c < boardSize && board[r][c] == opp) {
            r += dirs[d][0];
            c += dirs[d][1];
            len++;
        }
        if (len > 0 && r >= 0 && c >= 0 && r < boardSize && c < boardSize && board[r][c] == color)
            return true;
    }
    return false;
}
