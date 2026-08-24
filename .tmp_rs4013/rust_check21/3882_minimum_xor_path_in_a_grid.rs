struct Solution;
// LeetCode 3882 - Minimum XOR Path in a Grid
// https://leetcode.com/problems/minimum-xor-path-in-a-grid/

impl Solution {
    pub fn min_xor(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        let mut dp = vec![[false; 1024]; cols];
        for row in 0..rows {
            let mut left = [false; 1024];
            for col in 0..cols {
                let mut next = [false; 1024];
                let value = grid[row][col] as usize;
                if row == 0 && col == 0 {
                    next[value] = true;
                } else {
                    for xorv in 0..1024 {
                        if dp[col][xorv] || left[xorv] {
                            next[xorv ^ value] = true;
                        }
                    }
                }
                dp[col] = next;
                left = next;
            }
        }
        for xorv in 0..1024 {
            if dp[cols - 1][xorv] {
                return xorv as i32;
            }
        }
        -1
    }
}
