// LeetCode 1967 - Number of Strings That Appear as Substrings in Word
// https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

impl Solution {
    pub fn num_of_strings(patterns: Vec<String>, word: String) -> i32 {
        patterns.iter().filter(|p| word.contains(p.as_str())).count() as i32
    }
}
