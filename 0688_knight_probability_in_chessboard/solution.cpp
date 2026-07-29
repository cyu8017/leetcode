// LeetCode 0688 - Knight Probability in Chessboard
// https://leetcode.com/problems/knight-probability-in-chessboard/

#include <vector>

class Solution {
public:
    double knightProbability(int n, int k, int row, int column) {
        static const int moves[8][2] = {{-2, -1}, {-2, 1}, {-1, -2}, {-1, 2},
                                        {1, -2},  {1, 2},  {2, -1},  {2, 1}};
        std::vector<std::vector<double>> dp(n, std::vector<double>(n, 0.0));
        dp[row][column] = 1.0;
        for (int step = 0; step < k; ++step) {
            std::vector<std::vector<double>> nxt(n, std::vector<double>(n, 0.0));
            for (int r = 0; r < n; ++r) {
                for (int c = 0; c < n; ++c) {
                    if (dp[r][c] == 0.0) {
                        continue;
                    }
                    for (const auto& move : moves) {
                        const int nr = r + move[0];
                        const int nc = c + move[1];
                        if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                            nxt[nr][nc] += dp[r][c] / 8.0;
                        }
                    }
                }
            }
            dp.swap(nxt);
        }
        double total = 0.0;
        for (const auto& rowVals : dp) {
            for (double value : rowVals) {
                total += value;
            }
        }
        return total;
    }
};
