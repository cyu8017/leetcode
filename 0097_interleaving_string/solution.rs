// LeetCode 0097 - Interleaving String
// https://leetcode.com/problems/interleaving-string/

impl Solution {
    pub fn is_interleave(s1: String, s2: String, s3: String) -> bool {
        if s1.len() + s2.len() != s3.len() {
            return false;
        }

        let s1 = s1.as_bytes();
        let s2 = s2.as_bytes();
        let s3 = s3.as_bytes();
        let m = s1.len();
        let n = s2.len();
        let mut dp = vec![false; n + 1];
        dp[0] = true;

        for j in 1..=n {
            dp[j] = dp[j - 1] && s2[j - 1] == s3[j - 1];
        }

        for i in 1..=m {
            dp[0] = dp[0] && s1[i - 1] == s3[i - 1];
            for j in 1..=n {
                dp[j] = (dp[j] && s1[i - 1] == s3[i + j - 1])
                    || (dp[j - 1] && s2[j - 1] == s3[i + j - 1]);
            }
        }

        dp[n]
    }
}
