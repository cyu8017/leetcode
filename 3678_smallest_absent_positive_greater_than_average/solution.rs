// LeetCode 3678 - Smallest Absent Positive Greater Than Average
// https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

use std::collections::HashSet;

impl Solution {
    pub fn smallest_absent(nums: Vec<i32>) -> i32 {
        let mut s = HashSet::new();
        let mut sum = 0;
        for &x in &nums {
            s.insert(x);
            sum += x;
        }
        let mut ans = 1.max(sum / nums.len() as i32 + 1);
        while s.contains(&ans) {
            ans += 1;
        }
        ans
    }
}
