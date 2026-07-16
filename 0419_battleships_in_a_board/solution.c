// LeetCode 0419 - Battleships in a Board
// https://leetcode.com/problems/battleships-in-a-board/

int countBattleships(char** board, int boardSize, int* boardColSize) {
    int count = 0;
    int cols = boardColSize[0];

    for (int row = 0; row < boardSize; row++) {
        for (int col = 0; col < cols; col++) {
            if (board[row][col] != 'X') {
                continue;
            }
            if (row > 0 && board[row - 1][col] == 'X') {
                continue;
            }
            if (col > 0 && board[row][col - 1] == 'X') {
                continue;
            }
            count++;
        }
    }

    return count;
}
