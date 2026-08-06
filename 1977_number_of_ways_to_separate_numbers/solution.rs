// LeetCode 1977 - Number of Ways to Separate Numbers
// https://leetcode.com/problems/number-of-ways-to-separate-numbers/

impl Solution {
    pub fn number_of_combinations(num: String) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let num = num.as_bytes();
        let n = num.len();
        if num[0] == b'0' {
            return 0;
        }

        let mut lcp = vec![vec![0; n + 1]; n + 1];
        for i in (0..n).rev() {
            for j in (0..n).rev() {
                if num[i] == num[j] {
                    lcp[i][j] = lcp[i + 1][j + 1] + 1;
                }
            }
        }

        let le = |a: usize, b: usize, length: usize| -> bool {
            let common = lcp[a][b];
            if common >= length {
                return true;
            }
            num[a + common] < num[b + common]
        };

        let mut dp = vec![vec![0i32; n + 1]; n + 1];
        let mut pref = vec![vec![0i32; n + 1]; n + 1];

        for i in 1..=n {
            for l in 1..=i {
                let start = i - l;
                if num[start] == b'0' {
                    dp[i][l] = 0;
                } else if start == 0 {
                    dp[i][l] = 1;
                } else {
                    let mut ways = if l > 1 {
                        pref[start][(l - 1).min(start)]
                    } else {
                        0
                    };
                    if start >= l && le(start - l, start, l) {
                        ways = (ways + dp[start][l]) % MOD;
                    }
                    dp[i][l] = ways;
                }
            }
            for l in 1..=n {
                pref[i][l] = (pref[i][l - 1] + if l <= i { dp[i][l] } else { 0 }) % MOD;
            }
        }

        pref[n][n]
    }
}
