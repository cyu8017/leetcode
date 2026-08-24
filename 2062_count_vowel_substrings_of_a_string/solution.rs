// LeetCode 2062 - Count Vowel Substrings of a String
// https://leetcode.com/problems/count-vowel-substrings-of-a-string/

use std::collections::HashSet;

impl Solution {
    pub fn count_vowel_substrings(word: String) -> i32 {
        fn is_vowel(c: u8) -> bool {
            matches!(c, b'a' | b'e' | b'i' | b'o' | b'u')
        }
        let b = word.as_bytes();
        let mut ans = 0;
        for i in 0..b.len() {
            let mut seen = HashSet::new();
            for j in i..b.len() {
                if !is_vowel(b[j]) {
                    break;
                }
                seen.insert(b[j]);
                if seen.len() == 5 {
                    ans += 1;
                }
            }
        }
        ans
    }
}
