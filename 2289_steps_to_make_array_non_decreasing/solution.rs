// LeetCode 2289 - Steps to Make Array Non-decreasing
// https://leetcode.com/problems/steps-to-make-array-non-decreasing/

impl Solution {
    pub fn total_steps(nums: Vec<i32>) -> i32 {
        let mut stack: Vec<(i32, i32)> = Vec::new();
        let mut ans = 0;
        for i in (0..nums.len()).rev() {
            let mut steps = 0;
            while !stack.is_empty() && nums[i] > stack.last().unwrap().0 {
                steps = steps.max(stack.last().unwrap().1);
                stack.pop();
                steps += 1;
            }
            ans = ans.max(steps);
            stack.push((nums[i], steps));
        }
        ans
    }
}
