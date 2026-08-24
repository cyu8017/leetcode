// LeetCode 2666 - Allow One Function Call
// https://leetcode.com/problems/allow-one-function-call/

impl Solution {
    pub fn once(f: impl Fn(i32) -> i32) -> impl FnMut(i32) -> Option<i32> {
        let mut called = false;
        move |arg| {
            if called {
                return None;
            }
            called = true;
            Some(f(arg))
        }
    }
}
