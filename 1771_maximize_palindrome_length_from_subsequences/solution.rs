// LeetCode 1771 - Maximize Palindrome Length From Subsequences
// https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/

impl Solution {
    pub fn longest_palindrome(word1: String, word2: String) -> i32 {
        let n1 = word1.len();
        let s: Vec<u8> = word1.bytes().chain(word2.bytes()).collect();
        let n = s.len();
        let mut dp = vec![vec![0i32; n]; n];
        let mut ans = 0i32;
        for i in (0..n).rev() {
            dp[i][i] = 1;
            for j in i + 1..n {
                if s[i] == s[j] {
                    dp[i][j] = if j == i + 1 { 2 } else { dp[i + 1][j - 1] + 2 };
                    if i < n1 && n1 <= j {
                        ans = ans.max(dp[i][j]);
                    }
                } else {
                    dp[i][j] = dp[i + 1][j].max(dp[i][j - 1]);
                }
            }
        }
        ans
    }
}
