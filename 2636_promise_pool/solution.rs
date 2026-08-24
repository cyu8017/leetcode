// LeetCode 2636 - Promise Pool
// https://leetcode.com/problems/promise-pool/

impl Solution {
    pub fn promise_pool(functions: Vec<fn() -> i32>, _n: i32) -> Vec<i32> {
        functions.into_iter().map(|f| f()).collect()
    }
}
