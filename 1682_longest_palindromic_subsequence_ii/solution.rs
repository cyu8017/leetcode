// LeetCode 1682 - Longest Palindromic Subsequence II
// https://leetcode.com/problems/longest-palindromic-subsequence-ii/

impl Solution {
    pub fn longest_palindrome_subseq(s: String) -> i32 {
        let s = s.as_bytes();
        let n = s.len();
        let mut dp = vec![vec![[0i32; 26]; n]; n];
        for length in 2..=n {
            for i in 0..=n - length {
                let j = i + length - 1;
                for c in 0..26 {
                    dp[i][j][c] = dp[i + 1][j][c].max(dp[i][j - 1][c]);
                }
                if s[i] == s[j] {
                    let c = (s[i] - b'a') as usize;
                    let mut inner = 0;
                    if length > 2 {
                        for x in 0..26 {
                            if x != c {
                                inner = inner.max(dp[i + 1][j - 1][x]);
                            }
                        }
                    }
                    dp[i][j][c] = dp[i][j][c].max(inner + 2);
                }
            }
        }
        *dp[0][n - 1].iter().max().unwrap()
    }
}
