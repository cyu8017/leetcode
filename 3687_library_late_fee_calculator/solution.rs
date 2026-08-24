// LeetCode 3687 - Library Late Fee Calculator
// https://leetcode.com/problems/library-late-fee-calculator/

impl Solution {
    pub fn late_fee(days_late: Vec<i32>) -> i32 {
        fn fee(x: i32) -> i32 {
            if x == 1 {
                1
            } else if x > 5 {
                3 * x
            } else {
                2 * x
            }
        }
        days_late.into_iter().map(fee).sum()
    }
}
