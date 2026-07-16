// LeetCode 0280 - Wiggle Sort
// https://leetcode.com/problems/wiggle-sort/

impl Solution {
    pub fn wiggle_sort(nums: &mut Vec<i32>) {
        for index in 1..nums.len() {
            if index % 2 == 1 && nums[index] < nums[index - 1] {
                nums.swap(index, index - 1);
            } else if index % 2 == 0 && nums[index] > nums[index - 1] {
                nums.swap(index, index - 1);
            }
        }
    }
}
