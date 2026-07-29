// LeetCode 0750 - Number Of Corner Rectangles
// https://leetcode.com/problems/number-of-corner-rectangles/

int countCornerRectangles(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0], ans = 0;
    for (int i = 0; i < m; i++) {
        for (int j = i + 1; j < m; j++) {
            int count = 0;
            for (int c = 0; c < n; c++) {
                if (grid[i][c] && grid[j][c]) count++;
            }
            ans += count * (count - 1) / 2;
        }
    }
    return ans;
}
