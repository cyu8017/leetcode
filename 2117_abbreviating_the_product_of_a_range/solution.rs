// LeetCode 2117 - Abbreviating the Product of a Range
// https://leetcode.com/problems/abbreviating-the-product-of-a-range/

impl Solution {
    pub fn abbreviate_product(left: i32, right: i32) -> String {
        let mut twos = 0i32;
        let mut fives = 0i32;
        for i in left..=right {
            let mut x = i;
            while x % 2 == 0 {
                twos += 1;
                x /= 2;
            }
            while x % 5 == 0 {
                fives += 1;
                x /= 5;
            }
        }
        let zeros = twos.min(fives);
        const MOD: i64 = 100_000_000_000;
        let mut prod = 1i64;
        let extra2 = twos - zeros;
        let extra5 = fives - zeros;
        let mut log_sum = 0.0f64;
        for i in left..=right {
            let mut x = i;
            while x % 2 == 0 {
                x /= 2;
            }
            while x % 5 == 0 {
                x /= 5;
            }
            prod = (prod * x as i64) % MOD;
            log_sum += (x as f64).log10();
        }
        for _ in 0..extra2 {
            prod = (prod * 2) % MOD;
            log_sum += 2.0f64.log10();
        }
        for _ in 0..extra5 {
            prod = (prod * 5) % MOD;
            log_sum += 5.0f64.log10();
        }
        let mut full_log = 0.0f64;
        for i in left..=right {
            full_log += (i as f64).log10();
        }
        let digits = full_log as i32 + 1;
        if digits <= 10 {
            let mut p = 1i64;
            for i in left..=right {
                p *= i as i64;
            }
            return p.to_string();
        }
        let frac = log_sum - log_sum.floor();
        let prefix = 10.0f64.powf(frac + 4.0) as i64;
        let suffix = prod % 100000;
        format!("{}e{}{:05}", prefix, zeros, suffix)
    }
}
