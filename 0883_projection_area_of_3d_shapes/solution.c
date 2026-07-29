// LeetCode 0883 - Projection Area of 3D Shapes
// https://leetcode.com/problems/projection-area-of-3d-shapes/

#define MAX(a,b) ((a)>(b)?(a):(b))

int projectionArea(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    int n = gridSize, ans = 0;
    for (int i = 0; i < n; i++) {
        int rowMax = 0, colMax = 0;
        for (int j = 0; j < n; j++) {
            if (grid[i][j]) ans++;
            rowMax = MAX(rowMax, grid[i][j]);
            colMax = MAX(colMax, grid[j][i]);
        }
        ans += rowMax + colMax;
    }
    return ans;
}
