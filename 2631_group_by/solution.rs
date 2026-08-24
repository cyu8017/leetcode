// LeetCode 2631 - Group By
// https://leetcode.com/problems/group-by/

use std::collections::HashMap;

impl Solution {
    pub fn group_by(arr: Vec<i32>, f: impl Fn(i32) -> String) -> HashMap<String, Vec<i32>> {
        let mut out: HashMap<String, Vec<i32>> = HashMap::new();
        for x in arr {
            out.entry(f(x)).or_default().push(x);
        }
        out
    }
}
