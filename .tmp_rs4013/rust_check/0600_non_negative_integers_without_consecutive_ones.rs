struct Solution;
// LeetCode 0600 - Non-negative Integers without Consecutive Ones
// https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

impl Solution {
    pub fn find_integers(n: i32) -> i32 {
        let mut fib = [0i32; 32];
        fib[0] = 1;
        fib[1] = 2;
        for i in 2..32 {
            fib[i] = fib[i - 1] + fib[i - 2];
        }
        let mut answer = 0;
        let mut prev_bit = 0;
        for bit in (0..=30).rev() {
            if n & (1 << bit) != 0 {
                answer += fib[bit as usize];
                if prev_bit == 1 {
                    return answer;
                }
                prev_bit = 1;
            } else {
                prev_bit = 0;
            }
        }
        answer + 1
    }
}

fn main() {}
