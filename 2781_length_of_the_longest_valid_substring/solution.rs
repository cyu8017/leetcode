// LeetCode 2781 - Length of the Longest Valid Substring
// https://leetcode.com/problems/length-of-the-longest-valid-substring/

use std::collections::HashSet;

impl Solution {
    pub fn longest_valid_substring(word: String, forbidden: Vec<String>) -> i32 {
        let forbid: HashSet<String> = forbidden.iter().cloned().collect();
        let max_len = forbidden.iter().map(|f| f.len()).max().unwrap_or(0);
        let n = word.len();
        let mut ans = 0i32;
        let mut right = n as i32 - 1;
        for left in (0..n).rev() {
            let mut k = left;
            while (k as i32) <= right && k - left + 1 <= max_len {
                if forbid.contains(&word[left..=k]) {
                    right = k as i32 - 1;
                    break;
                }
                k += 1;
            }
            ans = ans.max(right - left as i32 + 1);
        }
        ans
    }
}
