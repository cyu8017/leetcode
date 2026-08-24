// LeetCode 0807 - Max Increase to Keep City Skyline
// https://leetcode.com/problems/max-increase-to-keep-city-skyline/

impl Solution {
    pub fn max_increase_keeping_skyline(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut row_max = vec![0; m];
        let mut col_max = vec![0; n];
        for r in 0..m {
            for c in 0..n {
                row_max[r] = row_max[r].max(grid[r][c]);
                col_max[c] = col_max[c].max(grid[r][c]);
            }
        }
        let mut ans = 0;
        for r in 0..m {
            for c in 0..n {
                ans += row_max[r].min(col_max[c]) - grid[r][c];
            }
        }
        ans
    }
}
