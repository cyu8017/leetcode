// LeetCode 1119 - Remove Vowels from a String
// https://leetcode.com/problems/remove-vowels-from-a-string/

impl Solution {
    pub fn remove_vowels(s: String) -> String {
        s.chars()
            .filter(|&c| c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u')
            .collect()
    }
}
