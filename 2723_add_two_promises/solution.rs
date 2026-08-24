// LeetCode 2723 - Add Two Promises
// https://leetcode.com/problems/add-two-promises/

impl Solution {
    pub fn add_two_promises(promise1: impl Fn() -> i32, promise2: impl Fn() -> i32) -> i32 {
        promise1() + promise2()
    }
}
