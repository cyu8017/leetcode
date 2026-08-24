// LeetCode 3978 - Unique Middle Element
// https://leetcode.com/problems/unique-middle-element/

impl Solution {
    pub fn is_middle_element_unique(nums: Vec<i32>) -> bool {
        let mid = nums[nums.len() / 2];
        nums.iter().filter(|&&x| x == mid).count() == 1
    }
}
