// LeetCode 2011 - Final Value of Variable After Performing Operations
// https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

impl Solution {
    pub fn final_value_after_operations(operations: Vec<String>) -> i32 {
        let mut x = 0;
        for op in operations {
            if op.as_bytes()[1] == b'+' {
                x += 1;
            } else {
                x -= 1;
            }
        }
        x
    }
}
