// LeetCode 1197 - Minimum Knight Moves
// https://leetcode.com/problems/minimum-knight-moves/

#include <stdlib.h>

static int memo[301][301];

static int dfs(int a, int b) {
    if (a + b == 0) return 0;
    if (a + b == 2) return 2;
    if (memo[a][b] >= 0) return memo[a][b];
    int r1 = dfs(a > 1 ? a - 1 : 1 - a, b > 2 ? b - 2 : 2 - b);
    int r2 = dfs(a > 2 ? a - 2 : 2 - a, b > 1 ? b - 1 : 1 - b);
    int best = r1 < r2 ? r1 : r2;
    memo[a][b] = best + 1;
    return memo[a][b];
}

int minKnightMoves(int x, int y) {
    x = x < 0 ? -x : x;
    y = y < 0 ? -y : y;
    for (int i = 0; i <= 300; i++) {
        for (int j = 0; j <= 300; j++) memo[i][j] = -1;
    }
    return dfs(x, y);
}
