// LeetCode 0878 - Nth Magical Number
// https://leetcode.com/problems/nth-magical-number/

impl Solution {
    pub fn nth_magical_number(n: i32, a: i32, b: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn gcd(mut x: i64, mut y: i64) -> i64 {
            while y != 0 {
                let t = x % y;
                x = y;
                y = t;
            }
            x
        }
        let a = a as i64;
        let b = b as i64;
        let lcm = a / gcd(a, b) * b;
        let mut lo = 1i64;
        let mut hi = n as i64 * a.min(b);
        while lo < hi {
            let mid = (lo + hi) / 2;
            if mid / a + mid / b - mid / lcm >= n as i64 {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        (lo % MOD) as i32
    }
}
