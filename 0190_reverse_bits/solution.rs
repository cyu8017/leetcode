// LeetCode 0190 - Reverse Bits
// https://leetcode.com/problems/reverse-bits/

impl Solution {
    pub fn reverse_bits(mut n: u32) -> u32 {
        let mut result = 0;
        for _ in 0..32 {
            result = (result << 1) | (n & 1);
            n >>= 1;
        }
        result
    }
}