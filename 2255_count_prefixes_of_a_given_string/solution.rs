// LeetCode 2255 - Count Prefixes of a Given String
// https://leetcode.com/problems/count-prefixes-of-a-given-string/

impl Solution {
    pub fn count_prefixes(words: Vec<String>, s: String) -> i32 {
        words.iter().filter(|w| s.starts_with(w.as_str())).count() as i32
    }
}
