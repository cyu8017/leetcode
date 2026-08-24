// LeetCode 0962 - Maximum Width Ramp
// https://leetcode.com/problems/maximum-width-ramp/

impl Solution {
    pub fn max_width_ramp(nums: Vec<i32>) -> i32 {
        let mut stack = Vec::new();
        for i in 0..nums.len() {
            if stack.is_empty() || nums[*stack.last().unwrap()] > nums[i] {
                stack.push(i);
            }
        }
        let mut ans = 0;
        for j in (0..nums.len()).rev() {
            while !stack.is_empty() && nums[*stack.last().unwrap()] <= nums[j] {
                ans = ans.max((j - stack.pop().unwrap()) as i32);
            }
        }
        ans
    }
}
