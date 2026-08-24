// LeetCode 0883 - Projection Area of 3D Shapes
// https://leetcode.com/problems/projection-area-of-3d-shapes/

impl Solution {
    pub fn projection_area(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut top = 0;
        let mut front = 0;
        let mut side = 0;
        for i in 0..n {
            let mut row_max = 0;
            let mut col_max = 0;
            for j in 0..n {
                if grid[i][j] != 0 {
                    top += 1;
                }
                row_max = row_max.max(grid[i][j]);
                col_max = col_max.max(grid[j][i]);
            }
            front += row_max;
            side += col_max;
        }
        top + front + side
    }
}
