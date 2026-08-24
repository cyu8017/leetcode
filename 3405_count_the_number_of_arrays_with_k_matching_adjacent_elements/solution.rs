// LeetCode 3405 - Count the Number of Arrays with K Matching Adjacent Elements
// https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/

impl Solution {
    fn mod_pow(mut a: i64, mut e: i64, modulus: i32) -> i64 {
        if a < 0 {
            a = 0;
        }
        let mut r = 1i64;
        a %= modulus as i64;
        while e > 0 {
            if e & 1 == 1 {
                r = r * a % modulus as i64;
            }
            a = a * a % modulus as i64;
            e >>= 1;
        }
        r
    }

    fn comb(n: i32, k: i32, modulus: i32) -> i32 {
        if k < 0 || k > n {
            return 0;
        }
        let mut num = 1i64;
        let mut den = 1i64;
        for i in 0..k {
            num = num * (n - i) as i64 % modulus as i64;
            den = den * (i + 1) as i64 % modulus as i64;
        }
        (num * Self::mod_pow(den, modulus as i64 - 2, modulus) % modulus as i64) as i32
    }

    pub fn count_good_arrays(n: i32, m: i32, k: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        (Self::comb(n - 1, k, MOD) as i64 * m as i64 % MOD as i64
            * Self::mod_pow((m - 1) as i64, (n - 1 - k) as i64, MOD)
            % MOD as i64) as i32
    }
}
