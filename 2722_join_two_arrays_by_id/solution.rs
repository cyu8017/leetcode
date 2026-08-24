// LeetCode 2722 - Join Two Arrays by ID
// https://leetcode.com/problems/join-two-arrays-by-id/

use std::collections::BTreeMap;

impl Solution {
    pub fn join(
        arr1: Vec<BTreeMap<String, i32>>,
        arr2: Vec<BTreeMap<String, i32>>,
    ) -> Vec<BTreeMap<String, i32>> {
        let mut by_id: BTreeMap<i32, BTreeMap<String, i32>> = BTreeMap::new();
        let merge = |arr: Vec<BTreeMap<String, i32>>,
                     by_id: &mut BTreeMap<i32, BTreeMap<String, i32>>| {
            for obj in arr {
                let id = *obj.get("id").unwrap();
                let dest = by_id.entry(id).or_default();
                for (k, v) in obj {
                    dest.insert(k, v);
                }
            }
        };
        merge(arr1, &mut by_id);
        merge(arr2, &mut by_id);
        by_id.into_values().collect()
    }
}
