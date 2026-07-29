// LeetCode 0782 - Transform to Chessboard
// https://leetcode.com/problems/transform-to-chessboard/

#include <algorithm>
#include <vector>

class Solution {
public:
    int movesToChessboard(std::vector<std::vector<int>>& board) {
        int n = static_cast<int>(board.size());
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) {
                    return -1;
                }
            }
        }
        int rowSum = 0;
        int colSum = 0;
        for (int i = 0; i < n; ++i) {
            rowSum += board[0][i];
            colSum += board[i][0];
        }
        if (!(n / 2 <= rowSum && rowSum <= (n + 1) / 2)) {
            return -1;
        }
        if (!(n / 2 <= colSum && colSum <= (n + 1) / 2)) {
            return -1;
        }
        int rowSwap = 0;
        int colSwap = 0;
        for (int i = 0; i < n; ++i) {
            rowSwap += board[0][i] != i % 2;
            colSwap += board[i][0] != i % 2;
        }
        if (n % 2) {
            if (rowSwap % 2) {
                rowSwap = n - rowSwap;
            }
            if (colSwap % 2) {
                colSwap = n - colSwap;
            }
        } else {
            rowSwap = std::min(rowSwap, n - rowSwap);
            colSwap = std::min(colSwap, n - colSwap);
        }
        return (rowSwap + colSwap) / 2;
    }
};
