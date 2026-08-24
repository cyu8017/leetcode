// LeetCode 3473 - Sum of K Subarrays With Length at Least M
// https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

impl Solution {
    pub fn max_sum(nums: Vec<i32>, k: i32, m: i32) -> i64 {
        let n = nums.len();
        let k = k as usize;
        let m = m as usize;
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i] as i64;
        }
        const NEG: i64 = -(1i64 << 60);
        let mut dp = vec![vec![NEG; n + 1]; k + 1];
        for i in 0..=n {
            dp[0][i] = 0;
        }
        for t in 1..=k {
            let mut best = NEG;
            for i in t * m..=n {
                let j = i - m;
                best = best.max(dp[t - 1][j] - pref[j]);
                dp[t][i] = best + pref[i];
            }
            for i in 1..=n {
                dp[t][i] = dp[t][i].max(dp[t][i - 1]);
            }
        }
        dp[k][n]
    }
}
