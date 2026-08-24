struct Solution;
// LeetCode 2930 - Number of Strings Which Can Be Rearranged to Contain Substring
// https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

impl Solution {
    pub fn string_count(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn mod_pow(mut a: i64, mut b: i32) -> i64 {
            const MOD: i64 = 1_000_000_007;
            let mut res = 1i64;
            a %= MOD;
            while b > 0 {
                if b & 1 == 1 {
                    res = res * a % MOD;
                }
                a = a * a % MOD;
                b >>= 1;
            }
            res
        }
        if n < 4 {
            return 0;
        }
        let mut ans = mod_pow(26, n);
        ans = (ans - 3 * mod_pow(25, n) % MOD + MOD) % MOD;
        ans = (ans + 3 * mod_pow(24, n) % MOD) % MOD;
        ans = (ans - mod_pow(23, n) + MOD) % MOD;
        ans = (ans + (n as i64 % MOD) * mod_pow(25, n - 1) % MOD) % MOD;
        ans = (ans - 2 * (n as i64 % MOD) % MOD * mod_pow(24, n - 1) % MOD + MOD) % MOD;
        ans = (ans + (n as i64 % MOD) * mod_pow(23, n - 1) % MOD) % MOD;
        ans = (ans
            - (n as i64 % MOD) * ((n - 1 + MOD as i32) as i64 % MOD) % MOD * mod_pow(24, n - 2) % MOD
                % MOD
            + MOD)
            % MOD;
        ans = (ans
            + (n as i64 % MOD) * ((n - 1 + MOD as i32) as i64 % MOD) % MOD * mod_pow(23, n - 2) % MOD)
            % MOD;
        ans as i32
    }
}

fn main() {}
