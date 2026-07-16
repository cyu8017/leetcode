// LeetCode 0396 - Rotate Function
// https://leetcode.com/problems/rotate-function/

impl Solution {
    pub fn max_rotate_function(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let total: i32 = nums.iter().sum();
        let mut current = nums
            .iter()
            .enumerate()
            .map(|(index, value)| index as i32 * value)
            .sum();
        let mut best = current;

        for index in (1..nums.len()).rev() {
            current += total - n * nums[index];
            best = best.max(current);
        }

        best
    }
}
