// LeetCode 1444 - Number of Ways of Cutting a Pizza
// https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

impl Solution {
    pub fn ways(pizza: Vec<String>, k: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let rows = pizza.len();
        let cols = pizza[0].len();
        let pizza: Vec<Vec<u8>> = pizza.into_iter().map(|s| s.into_bytes()).collect();
        let mut apples = vec![vec![0; cols + 1]; rows + 1];
        for r in (0..rows).rev() {
            for c in (0..cols).rev() {
                apples[r][c] = i32::from(pizza[r][c] == b'A') + apples[r + 1][c] + apples[r][c + 1]
                    - apples[r + 1][c + 1];
            }
        }
        let mut dp = vec![vec![0; cols]; rows];
        for r in 0..rows {
            for c in 0..cols {
                dp[r][c] = if apples[r][c] > 0 { 1 } else { 0 };
            }
        }
        for _ in 1..k {
            let mut nxt = vec![vec![0; cols]; rows];
            for r in 0..rows {
                for c in 0..cols {
                    for nr in r + 1..rows {
                        if apples[r][c] > apples[nr][c] {
                            nxt[r][c] = (nxt[r][c] + dp[nr][c]) % MOD;
                        }
                    }
                    for nc in c + 1..cols {
                        if apples[r][c] > apples[r][nc] {
                            nxt[r][c] = (nxt[r][c] + dp[r][nc]) % MOD;
                        }
                    }
                }
            }
            dp = nxt;
        }
        dp[0][0]
    }
}
