// LeetCode 2295 - Replace Elements in an Array
// https://leetcode.com/problems/replace-elements-in-an-array/

use std::collections::HashMap;

impl Solution {
    pub fn array_change(mut nums: Vec<i32>, operations: Vec<Vec<i32>>) -> Vec<i32> {
        let mut pos = HashMap::new();
        for (i, &x) in nums.iter().enumerate() {
            pos.insert(x, i);
        }
        for op in operations {
            let i = pos[&op[0]];
            nums[i] = op[1];
            pos.remove(&op[0]);
            pos.insert(op[1], i);
        }
        nums
    }
}
