// LeetCode 1808 - Maximize Number of Nice Divisors
// https://leetcode.com/problems/maximize-number-of-nice-divisors/

impl Solution {
    pub fn max_nice_divisors(prime_factors: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        if prime_factors <= 3 {
            return prime_factors;
        }

        fn pow_mod(mut base: i64, mut exp: i64, modulus: i64) -> i64 {
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

        let n = prime_factors as i64;
        match n % 3 {
            0 => pow_mod(3, n / 3, MOD) as i32,
            1 => (pow_mod(3, n / 3 - 1, MOD) * 4 % MOD) as i32,
            _ => (pow_mod(3, n / 3, MOD) * 2 % MOD) as i32,
        }
    }
}
