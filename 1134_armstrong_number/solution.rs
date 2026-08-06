// LeetCode 1134 - Armstrong Number
// https://leetcode.com/problems/armstrong-number/

impl Solution {
    pub fn is_armstrong(n: i32) -> bool {
        let mut digits = 0;
        let mut x = n;
        while x > 0 {
            digits += 1;
            x /= 10;
        }
        let mut sum = 0;
        let mut x = n;
        while x > 0 {
            let d = x % 10;
            let mut p = 1;
            for _ in 0..digits {
                p *= d;
            }
            sum += p;
            x /= 10;
        }
        sum == n
    }
}
