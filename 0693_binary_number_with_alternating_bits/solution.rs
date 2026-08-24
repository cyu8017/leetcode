// LeetCode 0693 - Binary Number with Alternating Bits
// https://leetcode.com/problems/binary-number-with-alternating-bits/

impl Solution {
    pub fn has_alternating_bits(n: i32) -> bool {
        let x = (n as u32) ^ ((n as u32) >> 1);
        x & (x + 1) == 0
    }
}
