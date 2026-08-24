struct Solution;
// LeetCode 2472 - Maximum Number of Non-overlapping Palindrome Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

impl Solution {
    pub fn max_palindromes(s: String, k: i32) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let k = k as usize;
        let mut is_pal = vec![vec![false; n]; n];
        for i in 0..n {
            is_pal[i][i] = true;
        }
        for i in 0..n.saturating_sub(1) {
            is_pal[i][i + 1] = b[i] == b[i + 1];
        }
        for length in 3..=n {
            for i in 0..=n - length {
                let j = i + length - 1;
                is_pal[i][j] = b[i] == b[j] && is_pal[i + 1][j - 1];
            }
        }
        let mut dp = vec![0; n + 1];
        for i in (0..n).rev() {
            dp[i] = dp[i + 1];
            if i + k - 1 < n {
                for j in (i + k - 1)..n {
                    if is_pal[i][j] && 1 + dp[j + 1] > dp[i] {
                        dp[i] = 1 + dp[j + 1];
                    }
                }
            }
        }
        dp[0]
    }
}

fn main() {}
