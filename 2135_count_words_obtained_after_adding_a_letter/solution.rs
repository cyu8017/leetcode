// LeetCode 2135 - Count Words Obtained After Adding a Letter
// https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

use std::collections::HashSet;

impl Solution {
    fn mask(w: &str) -> i32 {
        let mut m = 0;
        for c in w.bytes() {
            m |= 1 << (c - b'a');
        }
        m
    }

    pub fn word_count(start_words: Vec<String>, target_words: Vec<String>) -> i32 {
        let have: HashSet<i32> = start_words.iter().map(|w| Self::mask(w)).collect();
        let mut ans = 0;
        for w in target_words {
            let m = Self::mask(&w);
            for c in w.bytes() {
                if have.contains(&(m ^ (1 << (c - b'a')))) {
                    ans += 1;
                    break;
                }
            }
        }
        ans
    }
}
