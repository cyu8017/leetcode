// LeetCode 1969 - Minimum Non-Zero Product of the Array Elements
// https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

impl Solution {
    pub fn min_non_zero_product(p: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mx = (1i64 << p) - 1;
        let exp = (1i64 << (p - 1)) - 1;
        ((mx % MOD) * Self::mod_pow((mx - 1) % MOD, exp, MOD) % MOD) as i32
    }

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
}
