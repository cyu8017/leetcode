// LeetCode 0782 - Transform to Chessboard
int movesToChessboard(int** board, int boardSize, int* boardColSize) {
    (void)boardColSize;
    int n = boardSize;
    for (int i = 0; i < n; i++) for (int j = 0; j < n; j++)
        if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) return -1;
    int rowSum = 0, colSum = 0, rowSwap = 0, colSwap = 0;
    for (int i = 0; i < n; i++) {
        rowSum += board[0][i];
        colSum += board[i][0];
        rowSwap += board[0][i] != i % 2;
        colSwap += board[i][0] != i % 2;
    }
    if (rowSum < n / 2 || rowSum > (n + 1) / 2) return -1;
    if (colSum < n / 2 || colSum > (n + 1) / 2) return -1;
    if (n % 2) {
        if (rowSwap % 2) rowSwap = n - rowSwap;
        if (colSwap % 2) colSwap = n - colSwap;
    } else {
        if (n - rowSwap < rowSwap) rowSwap = n - rowSwap;
        if (n - colSwap < colSwap) colSwap = n - colSwap;
    }
    return (rowSwap + colSwap) / 2;
}
