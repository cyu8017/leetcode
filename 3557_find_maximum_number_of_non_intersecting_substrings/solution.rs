// LeetCode 3557 - Find Maximum Number of Non Intersecting Substrings
// https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

use std::collections::HashMap;

impl Solution {
    pub fn max_substrings(word: String) -> i32 {
        let mut ans = 0;
        let mut first: HashMap<char, usize> = HashMap::new();
        for (i, c) in word.chars().enumerate() {
            if !first.contains_key(&c) {
                first.insert(c, i);
            } else if i - first[&c] + 1 >= 4 {
                ans += 1;
                first.clear();
            }
        }
        ans
    }
}
