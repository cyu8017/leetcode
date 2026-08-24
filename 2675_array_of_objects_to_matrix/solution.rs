// LeetCode 2675 - Array of Objects to Matrix
// https://leetcode.com/problems/array-of-objects-to-matrix/

use std::collections::{BTreeMap, BTreeSet};

impl Solution {
    pub fn json_to_matrix(arr: Vec<BTreeMap<String, String>>) -> Vec<Vec<String>> {
        let mut keys = BTreeSet::new();
        for obj in &arr {
            for k in obj.keys() {
                keys.insert(k.clone());
            }
        }
        let mut mat = vec![keys.iter().cloned().collect::<Vec<_>>()];
        for obj in &arr {
            let mut row = Vec::new();
            for k in &keys {
                row.push(obj.get(k).cloned().unwrap_or_default());
            }
            mat.push(row);
        }
        mat
    }
}
