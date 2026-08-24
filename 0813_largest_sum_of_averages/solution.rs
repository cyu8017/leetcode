// LeetCode 0813 - Largest Sum of Averages
// https://leetcode.com/problems/largest-sum-of-averages/

impl Solution {
    pub fn largest_sum_of_averages(nums: Vec<i32>, k: i32) -> f64 {
        let n = nums.len();
        let mut prefix = vec![0.0; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] + nums[i] as f64;
        }
        let average = |i: usize, j: usize| (prefix[j] - prefix[i]) / (j - i) as f64;
        let mut dp = vec![0.0; n];
        for i in 0..n {
            dp[i] = average(0, i + 1);
        }
        for groups in 2..=k {
            let mut nxt = vec![0.0; n];
            for i in (groups - 1) as usize..n {
                let mut best = 0.0;
                for j in (groups - 2) as usize..i {
                    best = best.max(dp[j] + average(j + 1, i + 1));
                }
                nxt[i] = best;
            }
            dp = nxt;
        }
        dp[n - 1]
    }
}
