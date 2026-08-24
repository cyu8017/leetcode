struct Solution;
// LeetCode 0581 - Shortest Unsorted Continuous Subarray
// https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

impl Solution {
    pub fn find_unsorted_subarray(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut left: i32 = -1;
        let mut right: i32 = -2;
        let mut max_seen = nums[0];
        let mut min_seen = nums[n - 1];
        for i in 0..n {
            max_seen = max_seen.max(nums[i]);
            if nums[i] < max_seen {
                right = i as i32;
            }
            let j = n - 1 - i;
            min_seen = min_seen.min(nums[j]);
            if nums[j] > min_seen {
                left = j as i32;
            }
        }
        right - left + 1
    }
}

fn main() {}
