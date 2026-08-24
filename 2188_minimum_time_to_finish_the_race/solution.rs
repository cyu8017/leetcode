// LeetCode 2188 - Minimum Time to Finish the Race
// https://leetcode.com/problems/minimum-time-to-finish-the-race/

impl Solution {
    pub fn minimum_finish_time(tires: Vec<Vec<i32>>, change_time: i32, num_laps: i32) -> i32 {
        let mut min_time = vec![1 << 30; 20];
        for tire in &tires {
            let f = tire[0] as i64;
            let r = tire[1] as i64;
            let mut t = f;
            let mut lap = f;
            for x in 1..20 {
                if t >= min_time[x] as i64 {
                    break;
                }
                min_time[x] = t as i32;
                lap *= r;
                if lap > change_time as i64 + f {
                    break;
                }
                t += lap;
            }
        }
        let n = num_laps as usize;
        let mut dp = vec![1 << 30; n + 1];
        dp[0] = -change_time;
        for i in 1..=n {
            for j in 1..=i.min(19) {
                dp[i] = dp[i].min(dp[i - j] + change_time + min_time[j]);
            }
        }
        dp[n]
    }
}
