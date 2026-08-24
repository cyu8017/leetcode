// LeetCode 2042 - Check if Numbers Are Ascending in a Sentence
// https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

impl Solution {
    pub fn are_numbers_ascending(s: String) -> bool {
        let mut prev = -1;
        for tok in s.split_whitespace() {
            if tok.as_bytes()[0].is_ascii_digit() {
                let v: i32 = tok.parse().unwrap();
                if v <= prev {
                    return false;
                }
                prev = v;
            }
        }
        true
    }
}
