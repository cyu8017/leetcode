// LeetCode 2088 - Count Fertile Pyramids in a Land
// https://leetcode.com/problems/count-fertile-pyramids-in-a-land/

impl Solution {
    fn count(g: &[Vec<i32>]) -> i32 {
        let m = g.len();
        let n = g[0].len();
        let mut dp = g.to_vec();
        let mut ans = 0;
        for i in (0..m.saturating_sub(1)).rev() {
            for j in 1..n.saturating_sub(1) {
                if g[i][j] == 1 {
                    dp[i][j] = 1 + dp[i + 1][j - 1].min(dp[i + 1][j]).min(dp[i + 1][j + 1]);
                    ans += dp[i][j] - 1;
                }
            }
        }
        ans
    }

    pub fn count_pyramids(grid: Vec<Vec<i32>>) -> i32 {
        let ans = Self::count(&grid);
        let rev: Vec<Vec<i32>> = grid.into_iter().rev().collect();
        ans + Self::count(&rev)
    }
}
