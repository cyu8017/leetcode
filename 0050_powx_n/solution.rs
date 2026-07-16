// LeetCode 0050 - Pow(x, n)
// https://leetcode.com/problems/powx-n/

impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        let mut exp = n as i64;
        if exp == 0 {
            return 1.0;
        }

        let mut base = x;
        if exp < 0 {
            base = 1.0 / base;
            exp = -exp;
        }

        let mut result = 1.0;
        let mut current = base;

        while exp != 0 {
            if exp & 1 != 0 {
                result *= current;
            }
            current *= current;
            exp >>= 1;
        }

        result
    }
}
