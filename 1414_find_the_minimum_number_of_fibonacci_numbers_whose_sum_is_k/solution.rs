// LeetCode 1414 - Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
// https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

impl Solution {
    pub fn find_min_fibonacci_numbers(mut k: i32) -> i32 {
        let mut fib = vec![1, 1];
        while *fib.last().unwrap() < k {
            let n = fib.len();
            fib.push(fib[n - 1] + fib[n - 2]);
        }
        let mut answer = 0;
        for &value in fib.iter().rev() {
            if value <= k {
                k -= value;
                answer += 1;
            }
        }
        answer
    }
}
