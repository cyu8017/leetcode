// LeetCode 0263 - Ugly Number
// https://leetcode.com/problems/ugly-number/

impl Solution {
    pub fn is_ugly(n: i32) -> bool {
        let mut value = n;
        if value <= 0 {
            return false;
        }
        for factor in [2, 3, 5] {
            while value % factor == 0 {
                value /= factor;
            }
        }
        value == 1
    }
}
