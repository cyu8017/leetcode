struct Solution;
// LeetCode 0665 - Non-decreasing Array
// https://leetcode.com/problems/non-decreasing-array/

impl Solution {
    pub fn check_possibility(mut nums: Vec<i32>) -> bool {
        let mut changed = false;
        for i in 1..nums.len() {
            if nums[i] >= nums[i - 1] {
                continue;
            }
            if changed {
                return false;
            }
            changed = true;
            if i >= 2 && nums[i] < nums[i - 2] {
                nums[i] = nums[i - 1];
            } else {
                nums[i - 1] = nums[i];
            }
        }
        true
    }
}

fn main() {}
