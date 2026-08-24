// LeetCode 3719 - Longest Balanced Subarray I
// https://leetcode.com/problems/longest-balanced-subarray-i/

use std::collections::HashSet;

impl Solution {
    pub fn longest_balanced(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            let mut vis = HashSet::new();
            let mut cnt = [0, 0];
            for j in i..n {
                if vis.insert(nums[j]) {
                    cnt[(nums[j] & 1) as usize] += 1;
                }
                if cnt[0] == cnt[1] {
                    ans = ans.max((j - i + 1) as i32);
                }
            }
        }
        ans
    }
}
