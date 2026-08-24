// LeetCode 3603 - Minimum Cost Path with Alternating Directions II
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

impl Solution {
    pub fn min_cost(m: i32, n: i32, wait_cost: Vec<Vec<i32>>) -> i64 {
        let m = m as usize;
        let n = n as usize;
        let entry = |i: usize, j: usize| (i as i64 + 1) * (j as i64 + 1);
        let mut dp = vec![vec![i64::MAX / 4; n]; m];
        dp[0][0] = entry(0, 0);
        for i in 0..m {
            for j in 0..n {
                if i == 0 && j == 0 {
                    continue;
                }
                if i > 0 {
                    let mut cand = dp[i - 1][j] + entry(i, j);
                    if !(i - 1 == 0 && j == 0) {
                        cand += wait_cost[i - 1][j] as i64;
                    }
                    dp[i][j] = dp[i][j].min(cand);
                }
                if j > 0 {
                    let mut cand = dp[i][j - 1] + entry(i, j);
                    if !(i == 0 && j - 1 == 0) {
                        cand += wait_cost[i][j - 1] as i64;
                    }
                    dp[i][j] = dp[i][j].min(cand);
                }
            }
        }
        dp[m - 1][n - 1]
    }
}
