// LeetCode 0688 - Knight Probability in Chessboard
// https://leetcode.com/problems/knight-probability-in-chessboard/

#include <string.h>

double knightProbability(int n, int k, int row, int column) {
    static const int dirs[8][2] = {{-2,-1},{-2,1},{-1,-2},{-1,2},{1,-2},{1,2},{2,-1},{2,1}};
    double dp[25][25];
    double nxt[25][25];
    memset(dp, 0, sizeof(dp));
    dp[row][column] = 1.0;
    for (int step = 0; step < k; step++) {
        memset(nxt, 0, sizeof(nxt));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dp[i][j] == 0) continue;
                for (int d = 0; d < 8; d++) {
                    int ni = i + dirs[d][0], nj = j + dirs[d][1];
                    if (ni >= 0 && ni < n && nj >= 0 && nj < n) nxt[ni][nj] += dp[i][j] / 8.0;
                }
            }
        }
        memcpy(dp, nxt, sizeof(dp));
    }
    double ans = 0;
    for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) ans += dp[i][j];
    return ans;
}
