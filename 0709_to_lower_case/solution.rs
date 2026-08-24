// LeetCode 0709 - To Lower Case
// https://leetcode.com/problems/to-lower-case/

impl Solution {
    pub fn to_lower_case(s: String) -> String {
        s.bytes()
            .map(|ch| {
                if ch.is_ascii_uppercase() {
                    (ch + 32) as char
                } else {
                    ch as char
                }
            })
            .collect()
    }
}
