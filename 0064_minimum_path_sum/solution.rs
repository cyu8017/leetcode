// LeetCode 0064 - Minimum Path Sum
// https://leetcode.com/problems/minimum-path-sum/

impl Solution {
    pub fn min_path_sum(mut grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();

        for i in 0..rows {
            for j in 0..cols {
                if i == 0 && j == 0 {
                    continue;
                }
                if i == 0 {
                    grid[i][j] += grid[i][j - 1];
                } else if j == 0 {
                    grid[i][j] += grid[i - 1][j];
                } else {
                    grid[i][j] += grid[i - 1][j].min(grid[i][j - 1]);
                }
            }
        }

        grid[rows - 1][cols - 1]
    }
}
