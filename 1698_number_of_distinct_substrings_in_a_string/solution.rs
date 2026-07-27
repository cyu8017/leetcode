// LeetCode 1698 - Number of Distinct Substrings in a String
// https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/

use std::collections::HashMap;

impl Solution {
    pub fn count_distinct(s: String) -> i32 {
        let s = s.as_bytes();
        let mut nodes: Vec<HashMap<u8, usize>> = vec![HashMap::new()];
        let mut ans = 0;
        for i in 0..s.len() {
            let mut idx = 0usize;
            for &c in &s[i..] {
                if let Some(&next) = nodes[idx].get(&c) {
                    idx = next;
                } else {
                    let next = nodes.len();
                    nodes[idx].insert(c, next);
                    nodes.push(HashMap::new());
                    ans += 1;
                    idx = next;
                }
            }
        }
        ans
    }
}
