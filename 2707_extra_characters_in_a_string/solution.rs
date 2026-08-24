// LeetCode 2707 - Extra Characters in a String
// https://leetcode.com/problems/extra-characters-in-a-string/

use std::collections::HashSet;

impl Solution {
    pub fn min_extra_char(s: String, dictionary: Vec<String>) -> i32 {
        let dict: HashSet<String> = dictionary.into_iter().collect();
        let n = s.len();
        let mut dp = vec![n as i32; n + 1];
        dp[0] = 0;
        for i in 0..n {
            dp[i + 1] = dp[i + 1].min(dp[i] + 1);
            for j in i + 1..=n {
                if dict.contains(&s[i..j]) {
                    dp[j] = dp[j].min(dp[i]);
                }
            }
        }
        dp[n]
    }
}
