// LeetCode 0324 - Wiggle Sort II
// https://leetcode.com/problems/wiggle-sort-ii/

impl Solution {
    pub fn wiggle_sort(nums: &mut Vec<i32>) {
        let mut sorted_nums = nums.clone();
        sorted_nums.sort_unstable();
        let mut left = (nums.len() - 1) / 2;
        let mut right = nums.len() - 1;
        for index in 0..nums.len() {
            if index % 2 == 0 {
                nums[index] = sorted_nums[left];
                left -= 1;
            } else {
                nums[index] = sorted_nums[right];
                right -= 1;
            }
        }
    }
}
