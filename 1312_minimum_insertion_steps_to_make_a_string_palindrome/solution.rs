// LeetCode 1312 - Minimum Insertion Steps to Make a String Palindrome
// https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

impl Solution {
    pub fn min_insertions(s: String) -> i32 {
        let s: Vec<char> = s.chars().collect();
        let n = s.len();
        if n == 0 {
            return 0;
        }
        let mut dp = vec![0; n];
        for left in (0..n.saturating_sub(1)).rev() {
            let mut diagonal = 0;
            for right in left + 1..n {
                let old = dp[right];
                dp[right] = if s[left] == s[right] {
                    diagonal
                } else {
                    1 + dp[right].min(dp[right - 1])
                };
                diagonal = old;
            }
        }
        dp[n - 1]
    }
}
