// LeetCode 0221 - Maximal Square
// https://leetcode.com/problems/maximal-square/

#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.empty()) {
            return 0;
        }
        int rows = matrix.size();
        int cols = matrix[0].size();
        vector<int> dp(cols + 1, 0);
        int maxSide = 0;
        int prev = 0;
        for (int row = 1; row <= rows; ++row) {
            for (int col = 1; col <= cols; ++col) {
                int temp = dp[col];
                if (matrix[row - 1][col - 1] == '1') {
                    dp[col] = min({dp[col], dp[col - 1], prev}) + 1;
                    maxSide = max(maxSide, dp[col]);
                } else {
                    dp[col] = 0;
                }
                prev = temp;
            }
        }
        return maxSide * maxSide;
    }
};
