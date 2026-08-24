// LeetCode 2400 - Number of Ways to Reach a Position After Exactly k Steps
// https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

impl Solution {
    pub fn number_of_ways(start_pos: i32, end_pos: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let diff = (end_pos - start_pos).abs();
        if diff > k || (k - diff) % 2 != 0 {
            return 0;
        }
        let r = (k + diff) / 2;
        fn mod_pow(mut a: i64, mut e: i32, m: i64) -> i64 {
            let mut res = 1i64;
            a %= m;
            while e > 0 {
                if e & 1 == 1 {
                    res = res * a % m;
                }
                a = a * a % m;
                e >>= 1;
            }
            res
        }
        fn comb(n: i32, r: i32, m: i64) -> i32 {
            if r < 0 || r > n {
                return 0;
            }
            let mut num = 1i64;
            let mut den = 1i64;
            for i in 0..r {
                num = num * (n - i) as i64 % m;
                den = den * (i + 1) as i64 % m;
            }
            (num * mod_pow(den, (m - 2) as i32, m) % m) as i32
        }
        comb(k, r, MOD)
    }
}
