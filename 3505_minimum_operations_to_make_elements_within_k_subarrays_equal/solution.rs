// LeetCode 3505 - Minimum Operations to Make Elements Within K Subarrays Equal
// https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

impl Solution {
    pub fn min_operations(nums: Vec<i32>, x: i32, k: i32) -> i64 {
        let n = nums.len();
        let x = x as usize;
        let k = k as usize;
        let mut min_ops = vec![0i64; n - x + 1];
        for i in 0..=n - x {
            let mut w = nums[i..i + x].to_vec();
            w.sort();
            let med = w[(x - 1) / 2];
            let mut ops = 0i64;
            for v in w {
                ops += (v - med).abs() as i64;
            }
            min_ops[i] = ops;
        }
        let inf = 1i64 << 62;
        let mut dp = vec![vec![inf; k + 1]; n + 1];
        dp[n][0] = 0;
        for i in (0..n).rev() {
            for j in 0..=k {
                dp[i][j] = dp[i + 1][j];
                if j > 0 && i + x <= n && min_ops[i] + dp[i + x][j - 1] < dp[i][j] {
                    dp[i][j] = min_ops[i] + dp[i + x][j - 1];
                }
            }
        }
        dp[0][k]
    }
}
