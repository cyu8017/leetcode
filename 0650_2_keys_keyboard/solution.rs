// LeetCode 0650 - 2 Keys Keyboard
// https://leetcode.com/problems/2-keys-keyboard/

impl Solution {
    pub fn min_steps(mut n: i32) -> i32 {
        let mut steps = 0;
        let mut factor = 2;
        while factor * factor <= n {
            while n % factor == 0 {
                steps += factor;
                n /= factor;
            }
            factor += 1;
        }
        if n > 1 {
            steps += n;
        }
        steps
    }
}
