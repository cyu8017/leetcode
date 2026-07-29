// LeetCode 0576 - Out of Boundary Paths
// https://leetcode.com/problems/out-of-boundary-paths/

#include <stdlib.h>
#include <string.h>

int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
    const int MOD = 1000000007;
    int** dp = (int**)malloc((size_t)m * sizeof(int*));
    int** nxt = (int**)malloc((size_t)m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        dp[i] = (int*)calloc((size_t)n, sizeof(int));
        nxt[i] = (int*)calloc((size_t)n, sizeof(int));
    }
    dp[startRow][startColumn] = 1;
    int result = 0;
    int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    for (int move = 0; move < maxMove; move++) {
        for (int row = 0; row < m; row++) {
            memset(nxt[row], 0, (size_t)n * sizeof(int));
        }
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                int ways = dp[row][col];
                if (ways == 0) {
                    continue;
                }
                for (int d = 0; d < 4; d++) {
                    int nr = row + dirs[d][0];
                    int nc = col + dirs[d][1];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                        nxt[nr][nc] = (nxt[nr][nc] + ways) % MOD;
                    } else {
                        result = (result + ways) % MOD;
                    }
                }
            }
        }
        int** tmp = dp;
        dp = nxt;
        nxt = tmp;
    }

    for (int i = 0; i < m; i++) {
        free(dp[i]);
        free(nxt[i]);
    }
    free(dp);
    free(nxt);
    return result;
}
