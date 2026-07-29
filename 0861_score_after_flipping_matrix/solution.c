// LeetCode 0861 - Score After Flipping Matrix
// https://leetcode.com/problems/score-after-flipping-matrix/

#define MAX(a,b) ((a)>(b)?(a):(b))

int matrixScore(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    for (int i = 0; i < m; i++) {
        if (grid[i][0] == 0)
            for (int j = 0; j < n; j++) grid[i][j] ^= 1;
    }
    int ans = m * (1 << (n - 1));
    for (int j = 1; j < n; j++) {
        int ones = 0;
        for (int i = 0; i < m; i++) ones += grid[i][j];
        ans += MAX(ones, m - ones) * (1 << (n - 1 - j));
    }
    return ans;
}
