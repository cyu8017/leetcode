// LeetCode 0991 - Broken Calculator
// https://leetcode.com/problems/broken-calculator/

impl Solution {
    pub fn broken_calc(start_value: i32, mut target: i32) -> i32 {
        let mut ans = 0;
        while target > start_value {
            if target % 2 == 1 {
                target += 1;
            } else {
                target /= 2;
            }
            ans += 1;
        }
        ans + start_value - target
    }
}
