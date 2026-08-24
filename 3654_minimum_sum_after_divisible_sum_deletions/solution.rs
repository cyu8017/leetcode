// LeetCode 3654 - Minimum Sum After Divisible Sum Deletions
// https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

impl Solution {
    pub fn min_array_sum(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let k = k as usize;
        let mut prefix = vec![0usize; n + 1];
        for i in 0..n {
            prefix[i + 1] = (prefix[i] + nums[i] as usize) % k;
        }
        let inf = 1i64 << 62;
        let mut dp = vec![0i64; n + 1];
        let mut best = vec![inf; k];
        best[0] = 0;
        for i in 1..=n {
            dp[i] = dp[i - 1] + nums[i - 1] as i64;
            if best[prefix[i]] < dp[i] {
                dp[i] = best[prefix[i]];
            }
            if dp[i] < best[prefix[i]] {
                best[prefix[i]] = dp[i];
            }
        }
        dp[n]
    }
}
