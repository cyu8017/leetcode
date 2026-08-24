// LeetCode 0828 - Count Unique Characters of All Substrings of a Given String
// https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

use std::collections::HashMap;

impl Solution {
    pub fn unique_letter_string(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let n = chars.len() as i32;
        let mut last: HashMap<char, Vec<i32>> = HashMap::new();
        for &ch in &chars {
            last.entry(ch).or_insert_with(|| vec![-1]);
        }
        for (i, &ch) in chars.iter().enumerate() {
            last.get_mut(&ch).unwrap().push(i as i32);
        }
        for indices in last.values_mut() {
            indices.push(n);
        }
        let mut ans = 0;
        for indices in last.values() {
            for k in 1..indices.len() - 1 {
                ans += (indices[k] - indices[k - 1]) * (indices[k + 1] - indices[k]);
            }
        }
        ans
    }
}
