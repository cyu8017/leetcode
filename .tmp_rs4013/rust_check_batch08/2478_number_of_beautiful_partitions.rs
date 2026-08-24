struct Solution;
// LeetCode 2478 - Number of Beautiful Partitions
// https://leetcode.com/problems/number-of-beautiful-partitions/

impl Solution {
    pub fn beautiful_partitions(s: String, k: i32, min_length: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        fn is_prime(c: u8) -> bool {
            matches!(c, b'2' | b'3' | b'5' | b'7')
        }
        let b = s.as_bytes();
        let n = b.len();
        if !is_prime(b[0]) || is_prime(b[n - 1]) {
            return 0;
        }
        let k = k as usize;
        let min_length = min_length as usize;
        let mut dp = vec![vec![0; n + 1]; k + 1];
        dp[0][0] = 1;
        for p in 1..=k {
            let mut pref = 0;
            let mut j = 0;
            for i in 1..=n {
                while j + min_length <= i {
                    if j == 0 || (is_prime(b[j]) && !is_prime(b[j - 1])) {
                        pref = (pref + dp[p - 1][j]) % MOD;
                    }
                    j += 1;
                }
                if !is_prime(b[i - 1]) {
                    dp[p][i] = pref;
                }
            }
        }
        dp[k][n]
    }
}

fn main() {}
