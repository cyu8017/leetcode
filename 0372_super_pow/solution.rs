// LeetCode 0372 - Super Pow
// https://leetcode.com/problems/super-pow/

impl Solution {
    pub fn super_pow(a: i32, b: Vec<i32>) -> i32 {
        const MOD: i64 = 1337;
        let mut a = (a as i64).rem_euclid(MOD);
        let mut result = 1_i64;

        for digit in b {
            result = Self::pow_mod(result, 10, MOD) * Self::pow_mod(a, digit as i64, MOD) % MOD;
        }

        result as i32
    }

    fn pow_mod(mut base: i64, mut exponent: i64, modulo: i64) -> i64 {
        let mut result = 1_i64;
        base %= modulo;

        while exponent > 0 {
            if exponent & 1 == 1 {
                result = result * base % modulo;
            }
            base = base * base % modulo;
            exponent >>= 1;
        }

        result
    }
}
