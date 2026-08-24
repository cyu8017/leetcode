// LeetCode 2334 - Subarray With Elements Greater Than Varying Threshold
// https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/

impl Solution {
    pub fn valid_subarray_size(nums: Vec<i32>, threshold: i32) -> i32 {
        let n = nums.len();
        let mut left = vec![0i32; n];
        let mut right = vec![0i32; n];
        let mut stack: Vec<usize> = Vec::new();
        for i in 0..n {
            while !stack.is_empty() && nums[*stack.last().unwrap()] >= nums[i] {
                stack.pop();
            }
            left[i] = if stack.is_empty() { -1 } else { *stack.last().unwrap() as i32 };
            stack.push(i);
        }
        stack.clear();
        for i in (0..n).rev() {
            while !stack.is_empty() && nums[*stack.last().unwrap()] >= nums[i] {
                stack.pop();
            }
            right[i] = if stack.is_empty() { n as i32 } else { *stack.last().unwrap() as i32 };
            stack.push(i);
        }
        for i in 0..n {
            let k = right[i] - left[i] - 1;
            if nums[i] > threshold / k {
                return k;
            }
        }
        -1
    }
}
