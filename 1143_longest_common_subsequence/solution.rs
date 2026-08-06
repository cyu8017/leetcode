// LeetCode 1143 - Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/

impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let a = text1.as_bytes();
        let b = text2.as_bytes();
        let m = a.len();
        let n = b.len();
        let mut dp = vec![0; n + 1];
        for i in 1..=m {
            let mut prev = 0;
            for j in 1..=n {
                let cur = dp[j];
                if a[i - 1] == b[j - 1] {
                    dp[j] = prev + 1;
                } else {
                    dp[j] = dp[j].max(dp[j - 1]);
                }
                prev = cur;
            }
        }
        dp[n]
    }
}
