// LeetCode 0387 - First Unique Character in a String
// https://leetcode.com/problems/first-unique-character-in-a-string/

impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let mut counts = [0i32; 26];

        for ch in s.bytes() {
            counts[(ch - b'a') as usize] += 1;
        }

        for (index, ch) in s.bytes().enumerate() {
            if counts[(ch - b'a') as usize] == 1 {
                return index as i32;
            }
        }

        -1
    }
}
