struct Solution;
// LeetCode 2513 - Minimize the Maximum of Two Arrays
// https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

impl Solution {
    pub fn minimize_set(divisor1: i32, divisor2: i32, unique_cnt1: i32, unique_cnt2: i32) -> i32 {
        fn gcd(mut x: i64, mut y: i64) -> i64 {
            while y != 0 {
                let t = x % y;
                x = y;
                y = t;
            }
            x
        }
        let lcm = divisor1 as i64 / gcd(divisor1 as i64, divisor2 as i64) * divisor2 as i64;
        let ok = |x: i64| {
            let a = x - x / divisor1 as i64;
            let b = x - x / divisor2 as i64;
            let both = x - x / lcm;
            a >= unique_cnt1 as i64 && b >= unique_cnt2 as i64 && both >= unique_cnt1 as i64 + unique_cnt2 as i64
        };
        let mut lo = 1i64;
        let mut hi = 1i64 << 62;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if ok(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo as i32
    }
}

fn main() {}
