// LeetCode 2131 - Longest Palindrome by Concatenating Two Letter Words
// https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

use std::collections::HashMap;

impl Solution {
    pub fn longest_palindrome(words: Vec<String>) -> i32 {
        let mut freq = HashMap::new();
        for w in &words {
            *freq.entry(w.clone()).or_insert(0) += 1;
        }
        let mut ans = 0;
        let mut center = false;
        let keys: Vec<String> = freq.keys().cloned().collect();
        for w in keys {
            let c = *freq.get(&w).unwrap_or(&0);
            let b = w.as_bytes();
            let rev = format!("{}{}", b[1] as char, b[0] as char);
            if b[0] == b[1] {
                ans += (c / 2) * 4;
                if c % 2 == 1 {
                    center = true;
                }
            } else if w < rev {
                ans += c.min(*freq.get(&rev).unwrap_or(&0)) * 4;
            }
        }
        if center {
            ans += 2;
        }
        ans
    }
}
