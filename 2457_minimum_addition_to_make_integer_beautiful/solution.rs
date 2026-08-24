// LeetCode 2457 - Minimum Addition to Make Integer Beautiful
// https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

impl Solution {
    pub fn make_integer_beautiful(n: i64, target: i32) -> i64 {
        fn digit_sum(mut x: i64) -> i32 {
            let mut s = 0;
            while x > 0 {
                s += (x % 10) as i32;
                x /= 10;
            }
            s
        }
        let orig = n;
        let mut n = n;
        let mut pow = 1i64;
        while digit_sum(n) > target {
            n = n / 10 + 1;
            pow *= 10;
        }
        n * pow - orig
    }
}
