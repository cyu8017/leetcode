// LeetCode 2463 - Minimum Total Distance Traveled
// https://leetcode.com/problems/minimum-total-distance-traveled/

impl Solution {
    pub fn minimum_total_distance(mut robot: Vec<i32>, mut factory: Vec<Vec<i32>>) -> i64 {
        robot.sort_unstable();
        factory.sort_unstable();
        let m = robot.len();
        let mut pos = Vec::new();
        for f in &factory {
            for _ in 0..f[1] {
                pos.push(f[0]);
            }
        }
        let n = pos.len();
        const INF: i64 = 1 << 60;
        let mut dp = vec![vec![INF; n + 1]; m + 1];
        for j in 0..=n {
            dp[0][j] = 0;
        }
        for i in 1..=m {
            for j in i..=n {
                dp[i][j] = dp[i][j - 1];
                let mut diff = robot[i - 1] as i64 - pos[j - 1] as i64;
                if diff < 0 {
                    diff = -diff;
                }
                if dp[i - 1][j - 1] + diff < dp[i][j] {
                    dp[i][j] = dp[i - 1][j - 1] + diff;
                }
            }
        }
        dp[m][n]
    }
}
