// LeetCode 0389 - Find the Difference
// https://leetcode.com/problems/find-the-difference/

impl Solution {
    pub fn find_the_difference(s: String, t: String) -> char {
        let mut xor_value = 0;

        for ch in s.bytes().chain(t.bytes()) {
            xor_value ^= ch as i32;
        }

        xor_value as u8 as char
    }
}
