// LeetCode 1684 - Count the Number of Consistent Strings
// https://leetcode.com/problems/count-the-number-of-consistent-strings/

impl Solution {
    pub fn count_consistent_strings(allowed: String, words: Vec<String>) -> i32 {
        let mut mask = 0u32;
        for c in allowed.bytes() {
            mask |= 1 << (c - b'a');
        }
        words
            .into_iter()
            .filter(|w| w.bytes().all(|c| mask & (1 << (c - b'a')) != 0))
            .count() as i32
    }
}
