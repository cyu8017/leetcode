// LeetCode 3597 - Partition String
// https://leetcode.com/problems/partition-string/

use std::collections::HashSet;

impl Solution {
    pub fn partition_string(s: String) -> Vec<String> {
        let mut vis = HashSet::new();
        let mut ans = Vec::new();
        let mut t = String::new();
        for c in s.chars() {
            t.push(c);
            if !vis.contains(&t) {
                vis.insert(t.clone());
                ans.push(t.clone());
                t.clear();
            }
        }
        ans
    }
}
