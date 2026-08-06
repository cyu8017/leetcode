// LeetCode 1216 - Valid Palindrome III
// https://leetcode.com/problems/valid-palindrome-iii/

impl Solution {
    pub fn is_valid_palindrome(s: String, k: i32) -> bool {
        let s = s.as_bytes();
        let n = s.len();
        if n == 0 {
            return true;
        }
        let mut dp = vec![0; n];
        for i in (0..n).rev() {
            let mut previous = 0;
            for j in i + 1..n {
                let old = dp[j];
                if s[i] == s[j] {
                    dp[j] = previous;
                } else {
                    dp[j] = 1 + dp[j].min(dp[j - 1]);
                }
                previous = old;
            }
        }
        dp[n - 1] <= k
    }
}
