// LeetCode 0704 - Binary Search
// https://leetcode.com/problems/binary-search/

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut left = 0i32;
        let mut right = nums.len() as i32 - 1;
        while left <= right {
            let mid = left + (right - left) / 2;
            if nums[mid as usize] == target {
                return mid;
            }
            if nums[mid as usize] < target {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        -1
    }
}
