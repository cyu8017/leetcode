struct Solution;
// LeetCode 3913 - Sort Vowels by Frequency
// https://leetcode.com/problems/sort-vowels-by-frequency/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn sort_vowels(s: String) -> String {
        let st: HashSet<char> = ['a', 'e', 'i', 'o', 'u'].into_iter().collect();
        let mut vowels = Vec::new();
        let mut cnt = HashMap::new();
        for c in s.chars() {
            if !st.contains(&c) {
                continue;
            }
            if !cnt.contains_key(&c) {
                vowels.push(c);
            }
            *cnt.entry(c).or_insert(0) += 1;
        }
        vowels.sort_by(|a, b| cnt[b].cmp(&cnt[a]));
        let mut ans: Vec<char> = s.chars().collect();
        let mut i = 0;
        for k in 0..ans.len() {
            if !st.contains(&ans[k]) {
                continue;
            }
            let ch = vowels[i];
            ans[k] = ch;
            *cnt.get_mut(&ch).unwrap() -= 1;
            if cnt[&ch] == 0 {
                i += 1;
            }
        }
        ans.into_iter().collect()
    }
}
