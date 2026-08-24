// LeetCode 2008 - Maximum Earnings From Taxi
// https://leetcode.com/problems/maximum-earnings-from-taxi/

impl Solution {
    pub fn max_taxi_earnings(_n: i32, mut rides: Vec<Vec<i32>>) -> i64 {
        rides.sort_unstable_by_key(|r| r[1]);
        let m = rides.len();
        let ends: Vec<i32> = rides.iter().map(|r| r[1]).collect();
        let mut dp = vec![0i64; m + 1];
        for i in 0..m {
            let start = rides[i][0];
            let end = rides[i][1];
            let tip = rides[i][2];
            let earn = end as i64 - start as i64 + tip as i64;
            let j = ends.partition_point(|&e| e <= start);
            dp[i + 1] = dp[i].max(earn + dp[j]);
        }
        dp[m]
    }
}
