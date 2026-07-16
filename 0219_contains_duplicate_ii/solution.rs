// LeetCode 0219 - Contains Duplicate II
// https://leetcode.com/problems/contains-duplicate-ii/

use std::collections::HashMap;

impl Solution {
    pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
        let mut last_index: HashMap<i32, i32> = HashMap::new();
        for (i, num) in nums.iter().enumerate() {
            if let Some(prev) = last_index.get(num) {
                if (i as i32) - prev <= k {
                    return true;
                }
            }
            last_index.insert(*num, i as i32);
        }
        false
    }
}
