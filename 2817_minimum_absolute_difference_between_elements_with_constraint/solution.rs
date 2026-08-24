// LeetCode 2817 - Minimum Absolute Difference Between Elements With Constraint
// https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

use std::collections::BTreeSet;

impl Solution {
    pub fn min_absolute_difference(nums: Vec<i32>, x: i32) -> i32 {
        if x == 0 {
            let mut ans = i32::MAX;
            for i in 1..nums.len() {
                ans = ans.min((nums[i] - nums[i - 1]).abs());
            }
            return ans;
        }
        let mut ans = i32::MAX;
        let mut arr = BTreeSet::new();
        let x = x as usize;
        for i in x..nums.len() {
            arr.insert(nums[i - x]);
            let cur = nums[i];
            if let Some(&v) = arr.range(cur..).next() {
                ans = ans.min(v - cur);
            }
            if let Some(&v) = arr.range(..cur).next_back() {
                ans = ans.min(cur - v);
            }
        }
        ans
    }
}
