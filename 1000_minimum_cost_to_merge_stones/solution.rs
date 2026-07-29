// LeetCode 1000 - Minimum Cost to Merge Stones
// https://leetcode.com/problems/minimum-cost-to-merge-stones/

impl Solution {
    pub fn merge_stones(stones: Vec<i32>, k: i32) -> i32 {
        let n = stones.len();
        let k = k as usize;
        if (n - 1) % (k - 1) != 0 {
            return -1;
        }
        let mut prefix = vec![0; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] + stones[i];
        }
        let mut dp = vec![vec![0i32; n]; n];
        for length in k..=n {
            for i in 0..=n - length {
                let j = i + length - 1;
                let mut best = i32::MAX;
                let mut m = i;
                while m < j {
                    best = best.min(dp[i][m] + dp[m + 1][j]);
                    m += k - 1;
                }
                dp[i][j] = best;
                if (length - 1) % (k - 1) == 0 {
                    dp[i][j] += prefix[j + 1] - prefix[i];
                }
            }
        }
        dp[0][n - 1]
    }
}
