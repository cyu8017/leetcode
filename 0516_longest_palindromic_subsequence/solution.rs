// LeetCode 0516 - Longest Palindromic Subsequence
// https://leetcode.com/problems/longest-palindromic-subsequence/

impl Solution {
    pub fn longest_palindrome_subseq(s: String) -> i32 {
        let bytes = s.as_bytes();
        let length = bytes.len();
        let mut dp = vec![vec![0; length]; length];
        for index in (0..length).rev() {
            dp[index][index] = 1;
            for end in index + 1..length {
                if bytes[index] == bytes[end] {
                    dp[index][end] = dp[index + 1][end - 1] + 2;
                } else {
                    dp[index][end] = dp[index + 1][end].max(dp[index][end - 1]);
                }
            }
        }
        dp[0][length - 1]
    }
}
