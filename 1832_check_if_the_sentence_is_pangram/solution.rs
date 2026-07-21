// LeetCode 1832 - Check if the Sentence Is Pangram
// https://leetcode.com/problems/check-if-the-sentence-is-pangram/

use std::collections::HashSet;

impl Solution {
    pub fn check_if_pangram(sentence: String) -> bool {
        sentence.chars().collect::<HashSet<_>>().len() == 26
    }
}
