// LeetCode 0893 - Groups of Special-Equivalent Strings
// https://leetcode.com/problems/groups-of-special-equivalent-strings/

use std::collections::HashSet;

impl Solution {
    pub fn num_special_equiv_groups(words: Vec<String>) -> i32 {
        let mut groups = HashSet::new();
        for w in words {
            let mut even = String::new();
            let mut odd = String::new();
            for (i, ch) in w.chars().enumerate() {
                if i % 2 == 0 {
                    even.push(ch);
                } else {
                    odd.push(ch);
                }
            }
            let mut even_chars: Vec<char> = even.chars().collect();
            let mut odd_chars: Vec<char> = odd.chars().collect();
            even_chars.sort_unstable();
            odd_chars.sort_unstable();
            groups.insert(format!(
                "{}|{}",
                even_chars.into_iter().collect::<String>(),
                odd_chars.into_iter().collect::<String>()
            ));
        }
        groups.len() as i32
    }
}
