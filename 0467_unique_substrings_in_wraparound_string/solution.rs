// LeetCode 0467 - Unique Substrings in Wraparound String
// https://leetcode.com/problems/unique-substrings-in-wraparound-string/

impl Solution {
    pub fn find_substring_in_wrapround_string(s: String) -> i32 {
        let mut counts = [0i32; 26];
        let bytes = s.as_bytes();
        let mut length = 0;

        for index in 0..bytes.len() {
            if index > 0 && (i32::from(bytes[index] - bytes[index - 1]) + 26) % 26 == 1 {
                length += 1;
            } else {
                length = 1;
            }
            let position = (bytes[index] - b'a') as usize;
            counts[position] = counts[position].max(length);
        }

        counts.iter().sum()
    }
}
