// LeetCode 3426 - Manhattan Distances of All Arrangements of Pieces
// https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/

impl Solution {
    fn mod_pow(mut a: i64, mut e: i64, modulus: i32) -> i64 {
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

    pub fn distance_sum(m: i32, n: i32, k: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        if k < 2 {
            return 0;
        }
        let total_cells = m * n;
        let pair_choose = Self::comb(total_cells - 2, k - 2, MOD);
        let mut sum_dist = 0i64;
        for d in 1..m {
            sum_dist += d as i64 * (m - d) as i64 * n as i64 * n as i64;
        }
        for d in 1..n {
            sum_dist += d as i64 * (n - d) as i64 * m as i64 * m as i64;
        }
        (sum_dist % MOD as i64 * pair_choose as i64 % MOD as i64) as i32
    }
}
