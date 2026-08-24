struct Solution;
// LeetCode 2430 - Maximum Deletions on a String
// https://leetcode.com/problems/maximum-deletions-on-a-string/

impl Solution {
    pub fn delete_string(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut lcp = vec![vec![0; n + 1]; n + 1];
        for i in (0..n).rev() {
            for j in (0..n).rev() {
                if b[i] == b[j] {
                    lcp[i][j] = lcp[i + 1][j + 1] + 1;
                }
            }
        }
        let mut dp = vec![0; n];
        for i in (0..n).rev() {
            dp[i] = 1;
            let mut len = 1;
            while i + 2 * len <= n {
                if lcp[i][i + len] >= len {
                    dp[i] = dp[i].max(1 + dp[i + len]);
                }
                len += 1;
            }
        }
        dp[0]
    }
}

fn main() {}
