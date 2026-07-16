// LeetCode 0052 - N-Queens II
// https://leetcode.com/problems/n-queens-ii/

#include <functional>
#include <unordered_set>

class Solution {
public:
    int totalNQueens(int n) {
        int count = 0;
        std::unordered_set<int> cols;
        std::unordered_set<int> diag1;
        std::unordered_set<int> diag2;

        std::function<void(int)> backtrack = [&](int row) {
            if (row == n) {
                ++count;
                return;
            }

            for (int col = 0; col < n; ++col) {
                if (cols.count(col) || diag1.count(row + col) || diag2.count(row - col)) {
                    continue;
                }

                cols.insert(col);
                diag1.insert(row + col);
                diag2.insert(row - col);
                backtrack(row + 1);
                cols.erase(col);
                diag1.erase(row + col);
                diag2.erase(row - col);
            }
        };

        backtrack(0);
        return count;
    }
};
