// LeetCode 3581 - Count Odd Letters from Number
// https://leetcode.com/problems/count-odd-letters-from-number/

impl Solution {
    pub fn count_odd_letters(mut n: i32) -> i32 {
        let d = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
        let mut mask = 0u32;
        while n > 0 {
            for c in d[(n % 10) as usize].bytes() {
                mask ^= 1 << (c - b'a');
            }
            n /= 10;
        }
        mask.count_ones() as i32
    }
}
