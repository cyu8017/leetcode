// LeetCode 3195 - Find the Minimum Area to Cover All Ones I
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

int minimumArea(int** grid, int gridSize, int* gridColSize) {
    int x1 = gridSize, y1 = gridColSize[0], x2 = 0, y2 = 0;
    for (int i = 0; i < gridSize; i++)
        for (int j = 0; j < gridColSize[0]; j++)
            if (grid[i][j] == 1) {
                if (i < x1) x1 = i; if (j < y1) y1 = j;
                if (i > x2) x2 = i; if (j > y2) y2 = j;
            }
    return (x2 - x1 + 1) * (y2 - y1 + 1);
}
