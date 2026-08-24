// LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
// https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

impl Solution {
    pub fn minimum_changes(s: String, k: i32) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut cost = vec![vec![1 << 20; n]; n];
        let semi_cost = |l: usize, r: usize| -> i32 {
            let length = r - l + 1;
            let mut best = 1 << 20;
            for d in 1..length {
                if length % d != 0 {
                    continue;
                }
                let mut chg = 0;
                for start in 0..d {
                    let mut chars = Vec::new();
                    let mut i = l + start;
                    while i <= r {
                        chars.push(bytes[i]);
                        i += d;
                    }
                    let mut a = 0;
                    let mut b = chars.len() - 1;
                    while a < b {
                        if chars[a] != chars[b] {
                            chg += 1;
                        }
                        a += 1;
                        b -= 1;
                    }
                }
                best = best.min(chg);
            }
            best
        };
        for i in 0..n {
            for j in i + 1..n {
                cost[i][j] = semi_cost(i, j);
            }
        }
        let k = k as usize;
        let mut dp = vec![vec![1 << 20; n + 1]; k + 1];
        dp[0][0] = 0;
        for p in 1..=k {
            for i in 1..=n {
                for t in 0..i.saturating_sub(1) {
                    let cand = dp[p - 1][t] + cost[t][i - 1];
                    if cand < dp[p][i] {
                        dp[p][i] = cand;
                    }
                }
            }
        }
        dp[k][n]
    }
}
