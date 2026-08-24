// LeetCode 0686 - Repeated String Match
// https://leetcode.com/problems/repeated-string-match/

impl Solution {
    pub fn repeated_string_match(a: String, b: String) -> i32 {
        let repeats = ((b.len() + a.len() - 1) / a.len()) as i32;
        let mut built = String::new();
        for _ in 0..repeats {
            built.push_str(&a);
        }
        if built.contains(&b) {
            return repeats;
        }
        built.push_str(&a);
        if built.contains(&b) {
            repeats + 1
        } else {
            -1
        }
    }
}
