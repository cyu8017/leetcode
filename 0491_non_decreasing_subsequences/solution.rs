// LeetCode 0491 - Non-decreasing Subsequences
// https://leetcode.com/problems/non-decreasing-subsequences/

use std::collections::{BTreeSet, HashSet};

impl Solution {
    pub fn find_subsequences(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result = BTreeSet::new();
        Self::backtrack(&nums, 0, &mut Vec::new(), &mut result);
        result.into_iter().collect()
    }

    fn backtrack(nums: &[i32], start: usize, path: &mut Vec<i32>, result: &mut BTreeSet<Vec<i32>>) {
        if path.len() >= 2 {
            result.insert(path.clone());
        }
        let mut used = HashSet::new();
        for index in start..nums.len() {
            if used.contains(&nums[index]) {
                continue;
            }
            if !path.is_empty() && nums[index] < *path.last().unwrap() {
                continue;
            }
            used.insert(nums[index]);
            path.push(nums[index]);
            Self::backtrack(nums, index + 1, path, result);
            path.pop();
        }
    }
}
