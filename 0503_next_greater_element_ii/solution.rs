// LeetCode 0503 - Next Greater Element II
// https://leetcode.com/problems/next-greater-element-ii/

impl Solution {
    pub fn next_greater_elements(nums: Vec<i32>) -> Vec<i32> {
        let length = nums.len();
        let mut result = vec![-1; length];
        let mut stack = Vec::new();

        for index in 0..length * 2 {
            let value = nums[index % length];
            while stack.last().copied().map_or(false, |top| nums[top] < value) {
                let top = stack.pop().unwrap();
                result[top] = value;
            }
            if index < length {
                stack.push(index);
            }
        }
        result
    }
}
