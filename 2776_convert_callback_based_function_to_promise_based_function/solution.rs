// LeetCode 2776 - Convert Callback Based Function to Promise Based Function
// https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/

impl Solution {
    pub fn promisify<F: Fn()>(_fn: F) -> Box<dyn Fn() -> i32> {
        Box::new(|| 0)
    }
}
