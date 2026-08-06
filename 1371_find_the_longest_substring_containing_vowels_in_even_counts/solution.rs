// LeetCode 1371 - Find the Longest Substring Containing Vowels in Even Counts
// https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

use std::collections::HashMap;

impl Solution {
    pub fn find_the_longest_substring(s: String) -> i32 {
        let vowels = b"aeiou";
        let mut first = HashMap::new();
        first.insert(0i32, -1i32);
        let mut mask = 0i32;
        let mut ans = 0;
        for (i, c) in s.bytes().enumerate() {
            if let Some(pos) = vowels.iter().position(|&v| v == c) {
                mask ^= 1 << pos;
            }
            if let Some(&prev) = first.get(&mask) {
                ans = ans.max(i as i32 - prev);
            } else {
                first.insert(mask, i as i32);
            }
        }
        ans
    }
}
