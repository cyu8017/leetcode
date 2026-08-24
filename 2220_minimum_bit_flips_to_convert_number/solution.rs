// LeetCode 2220 - Minimum Bit Flips to Convert Number
// https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

impl Solution {
    pub fn min_bit_flips(start: i32, goal: i32) -> i32 {
        let mut x = start ^ goal;
        let mut ans = 0;
        while x > 0 {
            ans += x & 1;
            x >>= 1;
        }
        ans
    }
}
