// LeetCode 2691 - Immutability Helper
// https://leetcode.com/problems/immutability-helper/

use std::collections::BTreeMap;

impl Solution {
    pub fn immutable_helper(
        obj: BTreeMap<String, i32>,
        mutators: Vec<Box<dyn Fn(&mut BTreeMap<String, i32>)>>,
    ) -> Vec<BTreeMap<String, i32>> {
        let mut out = Vec::new();
        for m in mutators {
            let mut copy = obj.clone();
            m(&mut copy);
            out.push(copy);
        }
        out
    }
}
