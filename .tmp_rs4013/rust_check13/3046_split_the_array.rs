#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3046 - Split the Array
// https://leetcode.com/problems/split-the-array/

impl Solution {
    pub fn is_possible_to_split(nums: Vec<i32>) -> bool {
        let mut cnt = [0i32; 101];
        for x in nums {
            cnt[x as usize] += 1;
            if cnt[x as usize] >= 3 {
                return false;
            }
        }
        true
    }
}
