// LeetCode 0946 - Validate Stack Sequences
// https://leetcode.com/problems/validate-stack-sequences/

impl Solution {
    pub fn validate_stack_sequences(pushed: Vec<i32>, popped: Vec<i32>) -> bool {
        let mut stack = Vec::new();
        let mut j = 0;
        for x in pushed {
            stack.push(x);
            while !stack.is_empty() && stack.last() == Some(&popped[j]) {
                stack.pop();
                j += 1;
            }
        }
        stack.is_empty()
    }
}
