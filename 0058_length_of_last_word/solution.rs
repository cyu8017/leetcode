// LeetCode 0058 - Length of Last Word
// https://leetcode.com/problems/length-of-last-word/

impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut length = 0;
        let mut i = bytes.len() as i32 - 1;

        while i >= 0 && bytes[i as usize] == b' ' {
            i -= 1;
        }

        while i >= 0 && bytes[i as usize] != b' ' {
            length += 1;
            i -= 1;
        }

        length
    }
}
