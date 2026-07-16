// LeetCode 0063 - Unique Paths II
// https://leetcode.com/problems/unique-paths-ii/

impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        if obstacle_grid[0][0] == 1 {
            return 0;
        }

        let rows = obstacle_grid.len();
        let cols = obstacle_grid[0].len();
        let mut row = vec![0; cols];
        row[0] = 1;

        for i in 0..rows {
            if obstacle_grid[i][0] == 1 {
                row[0] = 0;
            }

            for j in 1..cols {
                if obstacle_grid[i][j] == 1 {
                    row[j] = 0;
                } else {
                    row[j] += row[j - 1];
                }
            }
        }

        row[cols - 1]
    }
}
