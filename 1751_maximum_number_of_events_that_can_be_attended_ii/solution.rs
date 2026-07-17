// LeetCode 1751 - Maximum Number of Events That Can Be Attended II
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

impl Solution {
    pub fn max_value(events: Vec<Vec<i32>>, k: i32) -> i32 {
        let mut events = events;
        events.sort();
        let n = events.len();
        let k = k as usize;
        let starts: Vec<i32> = events.iter().map(|e| e[0]).collect();

        let mut dp = vec![vec![0i32; n + 1]; k + 1];
        for i in (0..n).rev() {
            let j = starts.partition_point(|&s| s <= events[i][1]);
            for remain in 1..=k {
                dp[remain][i] = dp[remain][i + 1].max(events[i][2] + dp[remain - 1][j]);
            }
        }
        dp[k][0]
    }
}
