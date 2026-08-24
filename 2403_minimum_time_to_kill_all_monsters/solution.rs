// LeetCode 2403 - Minimum Time to Kill All Monsters
// https://leetcode.com/problems/minimum-time-to-kill-all-monsters/

impl Solution {
    pub fn minimum_time(power: Vec<i32>) -> i64 {
        let n = power.len();
        let nmask = 1 << n;
        let mut dp = vec![i64::MAX / 4; nmask];
        dp[0] = 0;
        for mask in 0..nmask {
            let killed = mask.count_ones() as i64;
            let gain = killed + 1;
            for i in 0..n {
                if mask & (1 << i) != 0 {
                    continue;
                }
                let need = (power[i] as i64 + gain - 1) / gain;
                let nm = mask | (1 << i);
                dp[nm] = dp[nm].min(dp[mask] + need);
            }
        }
        dp[nmask - 1]
    }
}
