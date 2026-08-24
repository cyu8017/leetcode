// LeetCode 2648 - Generate Fibonacci Sequence
// https://leetcode.com/problems/generate-fibonacci-sequence/

impl Solution {
    pub fn fib_generator() -> impl FnMut() -> i32 {
        let mut a = 0;
        let mut b = 1;
        move || {
            let v = a;
            let na = b;
            b = a + b;
            a = na;
            v
        }
    }
}
