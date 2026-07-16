// LeetCode 0365 - Water and Jug Problem
// https://leetcode.com/problems/water-and-jug-problem/

impl Solution {
    pub fn can_measure_water(x: i32, y: i32, target: i32) -> bool {
        if target == 0 {
            return true;
        }
        if x + y < target {
            return false;
        }
        target % Self::gcd(x, y) == 0
    }

    fn gcd(mut a: i32, mut b: i32) -> i32 {
        while b != 0 {
            let remainder = a % b;
            a = b;
            b = remainder;
        }
        a
    }
}
