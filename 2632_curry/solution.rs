// LeetCode 2632 - Curry
// https://leetcode.com/problems/curry/

impl Solution {
    pub fn curry(f: impl Fn(Vec<i32>) -> i32, _arity: i32) -> impl Fn(Vec<i32>) -> i32 {
        move |args| f(args)
    }
}
