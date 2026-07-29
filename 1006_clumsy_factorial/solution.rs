// LeetCode 1006 - Clumsy Factorial
// https://leetcode.com/problems/clumsy-factorial/

impl Solution {
    pub fn clumsy(mut n: i32) -> i32 {
        let mut stack = vec![n];
        n -= 1;
        let mut op = 0;
        while n > 0 {
            match op % 4 {
                0 => {
                    let top = stack.pop().unwrap();
                    stack.push(top * n);
                }
                1 => {
                    let top = stack.pop().unwrap();
                    stack.push(top / n);
                }
                2 => stack.push(n),
                _ => stack.push(-n),
            }
            n -= 1;
            op += 1;
        }
        stack.iter().sum()
    }
}
