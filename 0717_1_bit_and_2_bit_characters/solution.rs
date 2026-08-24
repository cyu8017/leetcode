// LeetCode 0717 - 1-bit and 2-bit Characters
// https://leetcode.com/problems/1-bit-and-2-bit-characters/

impl Solution {
    pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
        let mut i = 0;
        let n = bits.len();
        while i + 1 < n {
            i += if bits[i] == 1 { 2 } else { 1 };
        }
        i == n - 1
    }
}
