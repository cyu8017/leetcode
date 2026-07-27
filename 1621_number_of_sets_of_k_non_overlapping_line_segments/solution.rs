// LeetCode 1621 - Number of Sets of K Non-Overlapping Line Segments
// https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

impl Solution {
    pub fn number_of_sets(n: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        Self::comb((n + k - 1) as i64, (2 * k) as i64, MOD) as i32
    }

    fn comb(n: i64, mut r: i64, modulus: i64) -> i64 {
        if r < 0 || r > n {
            return 0;
        }
        if r > n - r {
            r = n - r;
        }
        let mut num = 1i64;
        let mut den = 1i64;
        for i in 0..r {
            num = num * (n - i) % modulus;
            den = den * (i + 1) % modulus;
        }
        num * Self::mod_pow(den, modulus - 2, modulus) % modulus
    }

    fn mod_pow(mut base: i64, mut exp: i64, modulus: i64) -> i64 {
        let mut res = 1i64;
        base %= modulus;
        while exp > 0 {
            if exp & 1 == 1 {
                res = res * base % modulus;
            }
            base = base * base % modulus;
            exp >>= 1;
        }
        res
    }
}
