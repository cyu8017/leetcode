// LeetCode 1961 - Check If String Is a Prefix of Array
// https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

impl Solution {
    pub fn is_prefix_string(s: String, words: Vec<String>) -> bool {
        let mut built = String::new();
        for w in words {
            built.push_str(&w);
            if built == s {
                return true;
            }
            if built.len() > s.len() || !s.starts_with(&built) {
                return false;
            }
        }
        false
    }
}
