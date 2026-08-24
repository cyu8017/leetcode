// LeetCode 3667 - Sort Array By Absolute Value
// https://leetcode.com/problems/sort-array-by-absolute-value/

impl Solution {
    pub fn sort_by_absolute_value(mut nums: Vec<i32>) -> Vec<i32> {
        nums.sort_by_key(|a| a.abs());
        nums
    }
}
