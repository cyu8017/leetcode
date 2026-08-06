// LeetCode 1424 - Diagonal Traverse II
// https://leetcode.com/problems/diagonal-traverse-ii/

use std::collections::BTreeMap;

impl Solution {
    pub fn find_diagonal_order(nums: Vec<Vec<i32>>) -> Vec<i32> {
        let mut diagonals: BTreeMap<usize, Vec<i32>> = BTreeMap::new();
        for (row, values) in nums.iter().enumerate() {
            for (col, &value) in values.iter().enumerate() {
                diagonals.entry(row + col).or_default().push(value);
            }
        }
        diagonals
            .into_values()
            .flat_map(|v| v.into_iter().rev())
            .collect()
    }
}
