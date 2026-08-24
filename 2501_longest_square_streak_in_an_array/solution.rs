// LeetCode 2501 - Longest Square Streak in an Array
// https://leetcode.com/problems/longest-square-streak-in-an-array/

use std::collections::HashSet;

impl Solution {
    pub fn longest_square_streak(nums: Vec<i32>) -> i32 {
        let mut set: HashSet<i64> = nums.iter().map(|&x| x as i64).collect();
        let mut best = -1;
        for x in nums {
            if !set.contains(&(x as i64)) {
                continue;
            }
            let mut length = 0;
            let mut cur = x as i64;
            while set.contains(&cur) {
                length += 1;
                set.remove(&cur);
                if cur > 100000 {
                    break;
                }
                cur = cur * cur;
            }
            if length >= 2 && length > best {
                best = length;
            }
        }
        best
    }
}
