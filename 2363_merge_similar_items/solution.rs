// LeetCode 2363 - Merge Similar Items
// https://leetcode.com/problems/merge-similar-items/

use std::collections::BTreeMap;

impl Solution {
    pub fn merge_similar_items(items1: Vec<Vec<i32>>, items2: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut mp = BTreeMap::new();
        for it in items1 {
            *mp.entry(it[0]).or_insert(0) += it[1];
        }
        for it in items2 {
            *mp.entry(it[0]).or_insert(0) += it[1];
        }
        mp.into_iter().map(|(k, v)| vec![k, v]).collect()
    }
}
