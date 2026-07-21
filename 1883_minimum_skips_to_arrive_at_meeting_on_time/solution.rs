// LeetCode 1883 - Minimum Skips to Arrive at Meeting On Time
// https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

impl Solution {
    pub fn min_skips(dist: Vec<i32>, speed: i32, hours_before: i32) -> i32 {
        let limit = hours_before as i64 * speed as i64;
        let n = dist.len();
        const INF: i64 = i64::MAX / 4;
        let mut dp = vec![INF; n + 1];
        dp[0] = 0;
        for &road in &dist {
            let mut nxt = vec![INF; n + 1];
            for skips in 0..n {
                if dp[skips] == INF {
                    continue;
                }
                let ceiled = ((dp[skips] + road as i64 + speed as i64 - 1) / speed as i64)
                    * speed as i64;
                nxt[skips] = nxt[skips].min(ceiled);
                nxt[skips + 1] = nxt[skips + 1].min(dp[skips] + road as i64);
            }
            dp = nxt;
        }
        for (skips, total) in dp.iter().enumerate() {
            if *total <= limit {
                return skips as i32;
            }
        }
        -1
    }
}
