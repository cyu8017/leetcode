// LeetCode 2670 - Find the Distinct Difference Array
// https://leetcode.com/problems/find-the-distinct-difference-array/

use std::collections::HashSet;

impl Solution {
    pub fn distinct_difference_array(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut suf = vec![0; n + 1];
        let mut seen = HashSet::new();
        for i in (0..n).rev() {
            seen.insert(nums[i]);
            suf[i] = seen.len() as i32;
        }
        seen.clear();
        let mut ans = vec![0; n];
        for i in 0..n {
            seen.insert(nums[i]);
            ans[i] = seen.len() as i32 - suf[i + 1];
        }
        ans
    }
}
