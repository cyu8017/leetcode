// LeetCode 2742 - Painting the Walls
// https://leetcode.com/problems/painting-the-walls/

impl Solution {
    pub fn paint_walls(cost: Vec<i32>, time: Vec<i32>) -> i32 {
        let n = cost.len();
        let inf = 1i64 << 60;
        let mut dp = vec![inf; n + 1];
        dp[0] = 0;
        for i in 0..n {
            for j in (0..=n).rev() {
                let mut nj = j + time[i] as usize + 1;
                if nj > n {
                    nj = n;
                }
                if dp[j] + (cost[i] as i64) < dp[nj] {
                    dp[nj] = dp[j] + cost[i] as i64;
                }
            }
        }
        dp[n] as i32
    }
}
