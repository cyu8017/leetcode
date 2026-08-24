// LeetCode 2721 - Execute Asynchronous Functions in Parallel
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

impl Solution {
    pub fn promise_all(functions: Vec<fn() -> i32>) -> Vec<i32> {
        functions.into_iter().map(|f| f()).collect()
    }
}
