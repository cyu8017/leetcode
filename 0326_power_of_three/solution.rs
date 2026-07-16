// LeetCode 0326 - Power of Three
// https://leetcode.com/problems/power-of-three/

impl Solution {
    pub fn is_power_of_three(n: i32) -> bool {
        if n <= 0 {
            return false;
        }
        let mut value = n;
        while value % 3 == 0 {
            value /= 3;
        }
        value == 1
    }
}
