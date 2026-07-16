// LeetCode 0376 - Wiggle Subsequence
// https://leetcode.com/problems/wiggle-subsequence/

impl Solution {
    pub fn wiggle_max_length(nums: Vec<i32>) -> i32 {
        if nums.len() < 2 {
            return nums.len() as i32;
        }

        let mut up = 1;
        let mut down = 1;
        for index in 1..nums.len() {
            if nums[index] > nums[index - 1] {
                up = down + 1;
            } else if nums[index] < nums[index - 1] {
                down = up + 1;
            }
        }

        up.max(down)
    }
}
