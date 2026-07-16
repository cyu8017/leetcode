// LeetCode 0509 - Fibonacci Number
// https://leetcode.com/problems/fibonacci-number/

impl Solution {
    pub fn fib(n: i32) -> i32 {
        if n <= 1 {
            return n;
        }
        let mut previous = 0;
        let mut current = 1;
        for _ in 2..=n {
            let next = previous + current;
            previous = current;
            current = next;
        }
        current
    }
}
