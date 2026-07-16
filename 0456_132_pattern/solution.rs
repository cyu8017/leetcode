// LeetCode 0456 - 132 Pattern
// https://leetcode.com/problems/132-pattern/

impl Solution {
    pub fn find132pattern(nums: Vec<i32>) -> bool {
        let mut stack: Vec<i32> = Vec::new();
        let mut third = i32::MIN;

        for value in nums.into_iter().rev() {
            if value < third {
                return true;
            }
            while let Some(top) = stack.last().copied() {
                if value > top {
                    third = top;
                    stack.pop();
                } else {
                    break;
                }
            }
            stack.push(value);
        }
        false
    }
}
