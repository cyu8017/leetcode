// LeetCode 1318 - Minimum Flips to Make a OR b Equal to c
// https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

impl Solution {
    pub fn min_flips(mut a: i32, mut b: i32, mut c: i32) -> i32 {
        let mut flips = 0;
        while a != 0 || b != 0 || c != 0 {
            let (x, y, z) = (a & 1, b & 1, c & 1);
            flips += if z == 0 {
                x + y
            } else {
                i32::from(x == 0 && y == 0)
            };
            a >>= 1;
            b >>= 1;
            c >>= 1;
        }
        flips
    }
}
