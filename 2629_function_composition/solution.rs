// LeetCode 2629 - Function Composition
// https://leetcode.com/problems/function-composition/

impl Solution {
    pub fn compose(functions: Vec<fn(i32) -> i32>) -> impl Fn(i32) -> i32 {
        move |mut x| {
            for f in functions.iter().rev() {
                x = f(x);
            }
            x
        }
    }
}
