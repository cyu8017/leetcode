// LeetCode 0034 - Find First and Last Position of Element in Sorted Array
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

impl Solution {
    pub fn search_range(&self, nums: Vec<i32>, target: i32) -> Vec<i32> {
        let lower_bound = || {
            let mut left = 0;
            let mut right = nums.len();
            while left < right {
                let mid = left + (right - left) / 2;
                if nums[mid] < target {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            left
        };

        let upper_bound = || {
            let mut left = 0;
            let mut right = nums.len();
            while left < right {
                let mid = left + (right - left) / 2;
                if nums[mid] <= target {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            left
        };

        if nums.is_empty() {
            return vec![-1, -1];
        }

        let start = lower_bound();
        if start == nums.len() || nums[start] != target {
            return vec![-1, -1];
        }

        vec![start as i32, upper_bound() as i32 - 1]
    }
}
