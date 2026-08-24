// LeetCode 2667 - Create Hello World Function
// https://leetcode.com/problems/create-hello-world-function/

impl Solution {
    pub fn create_hello_world() -> impl Fn() -> String {
        || "Hello World".to_string()
    }
}
