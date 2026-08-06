// LeetCode 1278 - Palindrome Partitioning III
// https://leetcode.com/problems/palindrome-partitioning-iii/

impl Solution {
    pub fn palindrome_partition(s: String, k: i32) -> i32 {
        let s = s.as_bytes();
        let n = s.len();
        let k = k as usize;
        let mut cost = vec![vec![0; n]; n];
        for length in 2..=n {
            for i in 0..=n - length {
                let j = i + length - 1;
                let mut c = if s[i] != s[j] { 1 } else { 0 };
                if length > 2 {
                    c += cost[i + 1][j - 1];
                }
                cost[i][j] = c;
            }
        }
        let inf = n as i32 + 1;
        let mut dp = vec![vec![inf; n + 1]; k + 1];
        dp[0][0] = 0;
        for parts in 1..=k {
            for end in parts..=n {
                for start in (parts - 1)..end {
                    dp[parts][end] = dp[parts][end].min(dp[parts - 1][start] + cost[start][end - 1]);
                }
            }
        }
        dp[k][n]
    }
}
