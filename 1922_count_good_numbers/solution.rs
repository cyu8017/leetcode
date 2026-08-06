// LeetCode 1922 - Count Good Numbers
// https://leetcode.com/problems/count-good-numbers/

impl Solution {
    pub fn count_good_numbers(n: i64) -> i32 {
        const MOD: i64 = 1_000_000_007;

        fn mod_pow(mut base: i64, mut exp: i64, modulus: i64) -> i64 {
            let mut result = 1i64;
            base %= modulus;
            while exp > 0 {
                if exp & 1 == 1 {
                    result = result * base % modulus;
                }
                base = base * base % modulus;
                exp >>= 1;
            }
            result
        }

        (mod_pow(5, (n + 1) / 2, MOD) * mod_pow(4, n / 2, MOD) % MOD) as i32
    }
}
