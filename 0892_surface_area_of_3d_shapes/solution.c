// LeetCode 0892 - Surface Area of 3D Shapes
// https://leetcode.com/problems/surface-area-of-3d-shapes/

#define MIN(a,b) ((a)<(b)?(a):(b))

int surfaceArea(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    int n = gridSize, ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int v = grid[i][j];
            if (v) {
                ans += v * 4 + 2;
                if (i > 0) ans -= MIN(v, grid[i - 1][j]) * 2;
                if (j > 0) ans -= MIN(v, grid[i][j - 1]) * 2;
            }
        }
    }
    return ans;
}
