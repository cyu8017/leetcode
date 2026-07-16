// LeetCode 0051 - N-Queens
// https://leetcode.com/problems/n-queens/

#include <functional>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<std::vector<std::string>> solveNQueens(int n) {
        std::vector<std::vector<std::string>> result;
        std::unordered_set<int> cols;
        std::unordered_set<int> diag1;
        std::unordered_set<int> diag2;
        std::vector<std::string> board(n, std::string(n, '.'));

        std::function<void(int)> backtrack = [&](int row) {
            if (row == n) {
                result.push_back(board);
                return;
            }

            for (int col = 0; col < n; ++col) {
                if (cols.count(col) || diag1.count(row + col) || diag2.count(row - col)) {
                    continue;
                }

                cols.insert(col);
                diag1.insert(row + col);
                diag2.insert(row - col);
                board[row][col] = 'Q';

                backtrack(row + 1);

                cols.erase(col);
                diag1.erase(row + col);
                diag2.erase(row - col);
                board[row][col] = '.';
            }
        };

        backtrack(0);
        return result;
    }
};
