// LeetCode 2700 - Differences Between Two Objects
// https://leetcode.com/problems/differences-between-two-objects/

use std::collections::BTreeMap;

impl Solution {
    pub fn obj_diff(
        obj1: BTreeMap<String, i32>,
        obj2: BTreeMap<String, i32>,
    ) -> BTreeMap<String, Vec<i32>> {
        let mut diff = BTreeMap::new();
        for (k, v) in &obj1 {
            if let Some(&v2) = obj2.get(k) {
                if v2 != *v {
                    diff.insert(k.clone(), vec![*v, v2]);
                }
            }
        }
        diff
    }
}
