// LeetCode 3779 - Minimum Number Of Operations To Have Distinct Elements
// https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

use std::collections::HashSet;

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut st = HashSet::new();
        for i in (0..nums.len()).rev() {
            if st.contains(&nums[i]) {
                return (i / 3) as i32 + 1;
            }
            st.insert(nums[i]);
        }
        0
    }
}
