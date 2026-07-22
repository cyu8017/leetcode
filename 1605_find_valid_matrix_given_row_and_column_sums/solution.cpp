// LeetCode 1605 - Find Valid Matrix Given Row and Column Sums
// https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> restoreMatrix(std::vector<int>& rowSum, std::vector<int>& colSum) {
        const int m = static_cast<int>(rowSum.size());
        const int n = static_cast<int>(colSum.size());
        std::vector<std::vector<int>> ans(m, std::vector<int>(n, 0));
        int i = 0, j = 0;
        while (i < m && j < n) {
            const int x = std::min(rowSum[i], colSum[j]);
            ans[i][j] = x;
            rowSum[i] -= x;
            colSum[j] -= x;
            if (rowSum[i] == 0) {
                ++i;
            }
            if (colSum[j] == 0) {
                ++j;
            }
        }
        return ans;
    }
};
