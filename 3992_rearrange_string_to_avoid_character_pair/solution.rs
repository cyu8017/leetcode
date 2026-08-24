// LeetCode 3992 - Rearrange String to Avoid Character Pair
// https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/

impl Solution {
    pub fn rearrange_string(s: String, _x: char, y: char) -> String {
        let mut bytes = s.into_bytes();
        let mut i = 0;
        for j in 0..bytes.len() {
            if bytes[j] == y as u8 {
                bytes.swap(i, j);
                i += 1;
            }
        }
        String::from_utf8(bytes).unwrap()
    }
}
