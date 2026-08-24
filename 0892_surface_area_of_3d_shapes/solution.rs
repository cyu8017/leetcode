// LeetCode 0892 - Surface Area of 3D Shapes
// https://leetcode.com/problems/surface-area-of-3d-shapes/

impl Solution {
    pub fn surface_area(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut area = 0;
        for i in 0..n {
            for j in 0..n {
                if grid[i][j] != 0 {
                    area += grid[i][j] * 4 + 2;
                    if i > 0 {
                        area -= grid[i][j].min(grid[i - 1][j]) * 2;
                    }
                    if j > 0 {
                        area -= grid[i][j].min(grid[i][j - 1]) * 2;
                    }
                }
            }
        }
        area
    }
}
