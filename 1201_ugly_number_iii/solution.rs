// LeetCode 1201 - Ugly Number III
// https://leetcode.com/problems/ugly-number-iii/

impl Solution {
    pub fn nth_ugly_number(n: i32, a: i32, b: i32, c: i32) -> i32 {
        fn gcd(mut x: i64, mut y: i64) -> i64 {
            while y != 0 {
                let t = x % y;
                x = y;
                y = t;
            }
            x
        }
        fn lcm(x: i64, y: i64) -> i64 {
            x / gcd(x, y) * y
        }
        let (a, b, c, n) = (a as i64, b as i64, c as i64, n as i64);
        let ab = lcm(a, b);
        let ac = lcm(a, c);
        let bc = lcm(b, c);
        let abc = lcm(ab, c);
        let count = |x: i64| x / a + x / b + x / c - x / ab - x / ac - x / bc + x / abc;
        let mut lo = 1i64;
        let mut hi = 2_000_000_000i64;
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if count(mid) >= n {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo as i32
    }
}
