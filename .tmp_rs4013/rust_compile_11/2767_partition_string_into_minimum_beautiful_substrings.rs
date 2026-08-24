struct Solution;
fn main() {}

// LeetCode 2767 - Partition String Into Minimum Beautiful Substrings
// https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

use std::collections::HashSet;

impl Solution {
    pub fn minimum_beautiful_substrings(s: String) -> i32 {
        let n = s.len();
        let mut pow5 = HashSet::new();
        let mut x: i64 = 1;
        loop {
            let mut t = x;
            let mut b = String::new();
            while t > 0 {
                b.push(char::from(b'0' + (t & 1) as u8));
                t >>= 1;
            }
            let b: String = b.chars().rev().collect();
            let b = if b.is_empty() { "0".to_string() } else { b };
            if b.len() > n {
                break;
            }
            pow5.insert(b);
            x *= 5;
        }
        const INF: i32 = 1 << 30;
        let mut dp = vec![INF; n + 1];
        dp[0] = 0;
        let bytes = s.as_bytes();
        for i in 0..n {
            if dp[i] == INF || bytes[i] == b'0' {
                continue;
            }
            for j in i + 1..=n {
                if pow5.contains(&s[i..j]) {
                    dp[j] = dp[j].min(dp[i] + 1);
                }
            }
        }
        if dp[n] == INF { -1 } else { dp[n] }
    }
}
