// LeetCode 0999 - Available Captures for Rook
// https://leetcode.com/problems/available-captures-for-rook/

int numRookCaptures(char** board, int boardSize, int* boardColSize) {
    int m = boardSize, n = boardColSize[0];
    int r = -1, c = -1;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            if (board[i][j] == 'R') { r = i; c = j; }
    if (r < 0) return 0;
    int ans = 0;
    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
    for (int d = 0; d < 4; d++) {
        int i = r + dirs[d][0], j = c + dirs[d][1];
        while (i >= 0 && i < m && j >= 0 && j < n) {
            if (board[i][j] == 'B') break;
            if (board[i][j] == 'p') { ans++; break; }
            i += dirs[d][0]; j += dirs[d][1];
        }
    }
    return ans;
}
