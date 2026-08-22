// LeetCode 3239 - Minimum Number of Flips to Make Binary Grid Palindromic I
// https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/

static int min_i(int a, int b) { return a < b ? a : b; }

int minFlips(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    int cnt1 = 0, cnt2 = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n / 2; j++) {
            if (grid[i][j] != grid[i][n - j - 1]) cnt1++;
        }
    }
    for (int j = 0; j < n; j++) {
        for (int i = 0; i < m / 2; i++) {
            if (grid[i][j] != grid[m - i - 1][j]) cnt2++;
        }
    }
    return min_i(cnt1, cnt2);
}
