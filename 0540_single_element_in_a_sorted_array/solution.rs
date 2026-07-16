// LeetCode 0540 - Single Element in a Sorted Array
// https://leetcode.com/problems/single-element-in-a-sorted-array/

impl Solution {
    pub fn single_non_duplicate(nums: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = nums.len() as i32 - 1;

        while left < right {
            let mut mid = (left + right) / 2;
            if mid % 2 == 1 {
                mid -= 1;
            }
            if nums[mid as usize] == nums[mid as usize + 1] {
                left = mid + 2;
            } else {
                right = mid;
            }
        }
        nums[left as usize]
    }
}
