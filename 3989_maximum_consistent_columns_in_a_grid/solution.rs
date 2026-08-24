// LeetCode 3989 - Maximum Consistent Columns in a Grid
// https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/

impl Solution {
    pub fn max_consistent_columns(grid: Vec<Vec<i32>>, limit: i32) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut dp = vec![1; n];
        let mut ans = 1;
        for j in 0..n {
            dp[j] = 1;
            for i in 0..j {
                if dp[i] + 1 <= dp[j] {
                    continue;
                }
                let mut ok = true;
                for r in 0..m {
                    let d = (grid[r][j] - grid[r][i]).abs();
                    if d > limit {
                        ok = false;
                        break;
                    }
                }
                if ok {
                    dp[j] = dp[i] + 1;
                }
            }
            if dp[j] > ans {
                ans = dp[j];
            }
        }
        ans
    }
}
