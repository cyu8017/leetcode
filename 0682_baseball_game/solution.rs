// LeetCode 0682 - Baseball Game
// https://leetcode.com/problems/baseball-game/

impl Solution {
    pub fn cal_points(operations: Vec<String>) -> i32 {
        let mut stack = Vec::new();
        for op in operations {
            if op == "C" {
                stack.pop();
            } else if op == "D" {
                let last = *stack.last().unwrap();
                stack.push(last * 2);
            } else if op == "+" {
                let n = stack.len();
                stack.push(stack[n - 1] + stack[n - 2]);
            } else {
                stack.push(op.parse().unwrap());
            }
        }
        stack.iter().sum()
    }
}
