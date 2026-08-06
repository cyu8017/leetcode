// LeetCode 1952 - Three Divisors
// https://leetcode.com/problems/three-divisors/

impl Solution {
    pub fn is_three(n: i32) -> bool {
        let root = (n as f64).sqrt() as i32;
        if root * root != n || root < 2 {
            return false;
        }
        let mut i = 2;
        while i * i <= root {
            if root % i == 0 {
                return false;
            }
            i += 1;
        }
        true
    }
}
