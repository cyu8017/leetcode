// LeetCode 2693 - Call Function with Custom Context
// https://leetcode.com/problems/call-function-with-custom-context/

impl Solution {
    pub fn call(f: impl Fn(i32, i32) -> i32, ctx: i32, arg: i32) -> i32 {
        f(ctx, arg)
    }
}
