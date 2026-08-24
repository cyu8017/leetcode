// LeetCode 2822 - Inversion of Object
// https://leetcode.com/problems/inversion-of-object/

use std::collections::HashMap;

impl Solution {
    pub fn invert_object(obj: HashMap<String, String>) -> HashMap<String, Vec<String>> {
        let mut out: HashMap<String, Vec<String>> = HashMap::new();
        for (k, v) in obj {
            out.entry(v).or_default().push(k);
        }
        out
    }
}
