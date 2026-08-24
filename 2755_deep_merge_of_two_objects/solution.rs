// LeetCode 2755 - Deep Merge of Two Objects
// https://leetcode.com/problems/deep-merge-of-two-objects/

use std::collections::HashMap;

impl Solution {
    pub fn deep_merge(
        obj1: HashMap<String, String>,
        obj2: HashMap<String, String>,
    ) -> HashMap<String, String> {
        let mut out = obj1;
        for (k, v) in obj2 {
            out.insert(k, v);
        }
        out
    }
}
