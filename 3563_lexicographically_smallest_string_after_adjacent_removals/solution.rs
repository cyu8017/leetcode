// LeetCode 3563 - Lexicographically Smallest String After Adjacent Removals
// https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/

impl Solution {
    pub fn lexicographically_smallest_string(s: String) -> String {
        let n = s.len();
        let b = s.as_bytes();
        let mut dp = vec![vec![String::new(); n + 1]; n + 1];
        let is_consec = |a: u8, c: u8| {
            let d = (a as i32 - c as i32).abs();
            d == 1 || d == 25
        };
        for length in 1..=n {
            for i in 0..=n - length {
                let j = i + length;
                let mut min_str = format!("{}{}", b[i] as char, dp[i + 1][j]);
                for k in i + 1..j {
                    if is_consec(b[i], b[k]) && dp[i + 1][k].is_empty() {
                        let cand = &dp[k + 1][j];
                        if cand < &min_str {
                            min_str = cand.clone();
                        }
                    }
                }
                dp[i][j] = min_str;
            }
        }
        dp[0][n].clone()
    }
}
