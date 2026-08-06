// LeetCode 1959 - Minimum Total Space Wasted With K Resizing Operations
// https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/

impl Solution {
    pub fn min_space_wasted_k_resizing(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        const INF: i64 = 10i64.pow(18);
        let mut waste = vec![vec![0i64; n]; n];
        for i in 0..n {
            let mut mx = 0i64;
            let mut total = 0i64;
            for j in i..n {
                mx = mx.max(nums[j] as i64);
                total += nums[j] as i64;
                waste[i][j] = mx * (j - i + 1) as i64 - total;
            }
        }

        let segments = (k + 1) as usize;
        let mut dp = vec![vec![INF; segments + 1]; n + 1];
        dp[0][0] = 0;
        for i in 1..=n {
            for s in 1..=segments.min(i) {
                for p in (s - 1)..i {
                    dp[i][s] = dp[i][s].min(dp[p][s - 1] + waste[p][i - 1]);
                }
            }
        }
        (1..=segments).map(|s| dp[n][s]).min().unwrap() as i32
    }
}
