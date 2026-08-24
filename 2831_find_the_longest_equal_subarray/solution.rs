// LeetCode 2831 - Find the Longest Equal Subarray
// https://leetcode.com/problems/find-the-longest-equal-subarray/

use std::collections::HashMap;

impl Solution {
    pub fn longest_equal_subarray(nums: Vec<i32>, k: i32) -> i32 {
        let mut pos: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &v) in nums.iter().enumerate() {
            pos.entry(v).or_default().push(i);
        }
        let mut ans = 0i32;
        for p in pos.values() {
            let mut left = 0usize;
            for right in 0..p.len() {
                while p[right] - p[left] - (right - left) > k as usize {
                    left += 1;
                }
                ans = ans.max((right - left + 1) as i32);
            }
        }
        ans
    }
}
