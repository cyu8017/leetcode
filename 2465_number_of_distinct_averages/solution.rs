// LeetCode 2465 - Number of Distinct Averages
// https://leetcode.com/problems/number-of-distinct-averages/

use std::collections::HashSet;

impl Solution {
    pub fn distinct_averages(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let mut seen = HashSet::new();
        let mut l = 0;
        let mut r = nums.len() - 1;
        while l < r {
            seen.insert(nums[l] + nums[r]);
            l += 1;
            r -= 1;
        }
        seen.len() as i32
    }
}
