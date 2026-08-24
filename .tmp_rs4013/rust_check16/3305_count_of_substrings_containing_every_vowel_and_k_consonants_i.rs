struct Solution;
// LeetCode 3305 - Count of Substrings Containing Every Vowel and K Consonants I
// https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/

use std::collections::HashMap;

impl Solution {
    fn is_vowel(c: u8) -> bool {
        matches!(c, b'a' | b'e' | b'i' | b'o' | b'u')
    }

    fn at_least(word: &str, k: i32) -> i32 {
        let mut cnt: HashMap<u8, i32> = HashMap::new();
        let mut cons = 0;
        let mut l = 0;
        let mut ans = 0;
        let w = word.as_bytes();
        for r in 0..w.len() {
            let c = w[r];
            if Self::is_vowel(c) {
                *cnt.entry(c).or_insert(0) += 1;
            } else {
                cons += 1;
            }
            while cnt.len() == 5 && cons >= k {
                ans += (w.len() - r) as i32;
                let c2 = w[l];
                if Self::is_vowel(c2) {
                    let e = cnt.get_mut(&c2).unwrap();
                    *e -= 1;
                    if *e == 0 {
                        cnt.remove(&c2);
                    }
                } else {
                    cons -= 1;
                }
                l += 1;
            }
        }
        ans
    }

    pub fn count_of_substrings(word: String, k: i32) -> i32 {
        Self::at_least(&word, k) - Self::at_least(&word, k + 1)
    }
}

fn main() {}
